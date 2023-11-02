def solution():
    # Calculate the number of sentences Janice typed before taking a break
    sentences_typed_before_break = 6 * 20  # Janice types 6 sentences per minute, she typed for 20 minutes
    # Calculate the number of sentences Janice typed after taking a break and before erasing the incorrect sentences
    sentences_typed_after_break = 6 * 15  # Janice types 6 sentences per minute, she typed for 15 minutes
    # Calculate the total number of sentences typed before erasing incorrect sentences
    total_sentences_typed = sentences_typed_before_break + sentences_typed_after_break
    # Calculate the total number of sentences after erasing incorrect sentences
    total_sentences_after_erasing = total_sentences_typed - 40
    # Calculate the total number of sentences after the meeting
    total_sentences_after_meeting = total_sentences_after_erasing + (6 * 18)  # Janice types 6 sentences per minute, she typed for 18 minutes
    # Calculate the number of sentences Janice started with today
    sentences_started_today = total_sentences_after_meeting - 536
    result = sentences_started_today
    return result

print(solution())