def solution():
    # Calculate the number of sentences typed before the break
    sentences_typed_before_break = 6 * 20

    # Calculate the number of sentences typed after the break
    sentences_typed_after_break = 6 * (20 + 15)

    # Calculate the total number of sentences typed before the erasing
    total_sentences_typed_before_erasing = sentences_typed_before_break + sentences_typed_after_break

    # Calculate the total number of sentences typed after the erasing and meeting
    total_sentences_typed_after_erasing_and_meeting = 6 * 18 + total_sentences_typed_before_erasing - 40

    # Calculate the number of sentences she started with today
    sentences_started_today = 536 - total_sentences_typed_after_erasing_and_meeting

    result = sentences_started_today
    return result

print(solution())