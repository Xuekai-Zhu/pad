

model.eval()
        logger.info("*** Beam Searche Predict ***")
        evaluator = ReasoningEvaluator(
        # score_types=['faithfulness'],
        model_type="sim_sce",
        transformer_model="facebook/roscoe-512-roberta-base",)
        
        def generate_function_with_beam_search(inputs, beam_size, model, decoder_input_ids=None):
            batch_size = inputs.input_ids.size()[0]
            
            if decoder_input_ids is None:
                return_candicant = beam_size**2
                output = model.generate(inputs.input_ids.cuda(), 
                                        attention_mask=inputs.attention_mask.cuda(),
                                        num_beams=return_candicant, 
                                        num_return_sequences=return_candicant,
                                        max_length=data_args.max_target_length,
                                        return_dict_in_generate=True,
                                        output_scores=True,
                                        )
            else:
                return_candicant = beam_size
                # 1. expand input ids to decoder_ids size
                # input_ids = inputs.input_ids.repeat(1, return_candicant).view(training_args.per_device_eval_batch_size*beam_size, -1).cuda()
                
                input_ids = inputs.input_ids.repeat(1, beam_size).view(decoder_input_ids.input_ids.size()[0], -1).cuda()
                attention_mask = inputs.attention_mask.repeat(1, beam_size).view(decoder_input_ids.input_ids.size()[0], -1).cuda()
                # 2. genrerate
                output = model.generate(input_ids, 
                                        attention_mask=attention_mask,
                                        decoder_input_ids=decoder_input_ids.input_ids.cuda(),
                                        num_beams=return_candicant, 
                                        num_return_sequences=return_candicant,
                                        max_length=data_args.max_target_length,
                                        return_dict_in_generate=True,
                                        output_scores=True,
                                        )
            return output
            
        predict_dataset_loader = trainer.get_test_dataloader(predict_dataset)
        
        step_index = np.zeros(shape=(training_args.per_device_eval_batch_size * data_args.num_beams * data_args.num_beams), dtype=np.int32)
        max_auto_step = 24
        all_predict = []
        with torch.no_grad():
            for batch_i, inputs in enumerate(tqdm(predict_dataset_loader)):
                decoder_input = None
                step_index = np.zeros(shape=(training_args.per_device_eval_batch_size * data_args.num_beams * data_args.num_beams), dtype=np.int32)

                for step in range(max_auto_step):
                    if step == 0 or decoder_input == None:
                        # first generate 
                        output = generate_function_with_beam_search(inputs, data_args.num_beams, model)
                        
                        # transition_scores = model.compute_transition_scores(output.sequences, 
                        #                                                     output.scores, output.beam_indices, 
                        #                                                     normalize_logits=False)
                        # preparer context and reasoning step
                        input_context = tokenizer.batch_decode(inputs.input_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True) #* (data_args.num_beams**2)
                        input_context = list(np.repeat(input_context,data_args.num_beams**2))
                        output_sequence = tokenizer.batch_decode(output.sequences, skip_special_tokens=True, clean_up_tokenization_spaces=True)
                        
                        now_step, before_step = batch_parse_chain(output_sequence, type="code", index=step_index, return_before_step=True)
                        # print(now_step[0])

                        if "def solution():" in now_step or "returen result" in now_step:
                            step_index += 1
                            continue


                        evaluator.update_evaluator(context=input_context,
                                reasoning_code=now_step,
                                )
                        scores = evaluator.evaluate(score_types=['faithfulness'])['faithfulness']
                        
                        scores = np.array(scores).reshape(-1, data_args.num_beams**2)
                        before_step = np.array(before_step).reshape(-1, data_args.num_beams**2)
                        max_indices = np.argsort(scores, axis=-1)[:, :data_args.num_beams]
                        max_before_step = np.take_along_axis(before_step, max_indices, axis=-1).flatten().tolist()

                        # pass to next step
                        step_index += 1
                        decoder_input = max_before_step # batch * beam_size

                    
                    # after generate
                    else:
                        if np.all(step_index == -1):
                            all_predict.append(predictions[-1])
                            break
                        
                        decoder_input_ids = tokenizer(decoder_input, max_length=data_args.max_source_length, padding=True, truncation=True, return_tensors="pt")
                        output = generate_function_with_beam_search(inputs, data_args.num_beams, model, decoder_input_ids=decoder_input_ids)
                        output_sequence = tokenizer.batch_decode(output.sequences, skip_special_tokens=True, clean_up_tokenization_spaces=True)
                        now_step, before_step = batch_parse_chain(output_sequence, type="code", index=step_index, return_before_step=True)

                        
                        # ransition_scores = model.compute_transition_scores(output.sequences, 
                        #                                                 output.scores, output.beam_indices, 
                        #                                                 normalize_logits=False)
                        # print(ransition_scores.size())
                        # print(output.sequences.size())
                        
                        input_context = tokenizer.batch_decode(inputs.input_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True) #* (data_args.num_beams**2)
                        input_context = list(np.repeat(input_context,data_args.num_beams**2))
                        # output_sequence = tokenizer.batch_decode(output.sequences, skip_special_tokens=True, clean_up_tokenization_spaces=True)

                        evaluator.update_evaluator(context=input_context,
                                reasoning_code=now_step,
                                )
                        scores = evaluator.evaluate(score_types=['faithfulness'])['faithfulness']
                        
                        scores = np.array(scores).reshape(-1, data_args.num_beams**2)
                        before_step = np.array(before_step).reshape(-1, data_args.num_beams**2)
                        max_indices = np.argsort(scores, axis=-1)[:, :data_args.num_beams]

                        max_before_step = np.take_along_axis(before_step, max_indices, axis=-1).flatten().tolist()
                        decoder_input = max_before_step # batch * beam_size
                        
                        
                        # save 
                        predictions = tokenizer.batch_decode(
                            output.sequences, skip_special_tokens=True, clean_up_tokenization_spaces=True
                        )
                        # pass to next step
                        step_index += 1
                        for n, pre in enumerate(predictions):
                            if "return result" in pre:
                                step_index[n] = -1

            
            prediction_text = [json.dumps({"output":pred.strip()}) for pred in all_predict]
            output_prediction_file = os.path.join(training_args.output_dir, "generated_predictions.json")
            with open(output_prediction_file, "w") as writer:
                writer.write("\n".join(prediction_text))