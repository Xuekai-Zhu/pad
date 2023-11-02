def solution():
    """Meryll wants to write 35 multiple-choice questions and 15 problem-solving questions for her Chemistry class.
    She already has written 2/5 of the multiple-choice and 1/3 of the problem-solving questions.
    How many more questions does she need to write for both multiple-choice and problem-solving?"""
    
    total_mc_questions = 35
    total_ps_questions = 15
    
    # multiply the total number of MC questions by 2/5 to get the number of MC questions already written
    written_mc_questions = total_mc_questions * (2/5)
    
    # multiply the total number of PS questions by 1/3 to get the number of PS questions already written
    written_ps_questions = total_ps_questions * (1/3)
    
    # subtract the number of questions already written for both MC and PS from their respective totals to get the number of questions to be written
    mc_questions_to_be_written = total_mc_questions - written_mc_questions
    ps_questions_to_be_written = total_ps_questions - written_ps_questions
    
    total_questions_to_be_written = mc_questions_to_be_written + ps_questions_to_be_written
    
    result = total_questions_to_be_written
    
    return result

print(solution())