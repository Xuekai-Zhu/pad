def solution():
    """Janice can type 6 sentences per minute. Today at work, Janice continued working on a paper she started typing yesterday. She typed for 20 minutes, took a break, and typed 15 minutes longer. She then had to erase 40 sentences she had typed incorrectly. After a meeting, she typed for 18 minutes more. In all, the paper had 536 sentences by the end of today. How many sentences did she start with today?"""
    sentences_per_minute = 6
    initial_time = 20
    break_time = 15
    error_sentences = 40
    meeting_time = 18
    total_time = initial_time + break_time + meeting_time
    total_sentences_typed = total_time * sentences_per_minute - error_sentences
    initial_sentences = 536 - total_sentences_typed
    result = initial_sentences
    return result

print(solution())