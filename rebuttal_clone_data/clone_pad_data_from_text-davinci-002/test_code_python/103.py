def solution():
    """Janice can type 6 sentences per minute. Today at work, Janice continued working on a paper she started typing yesterday. She typed for 20 minutes, took a break, and typed 15 minutes longer. She then had to erase 40 sentences she had typed incorrectly. After a meeting, she typed for 18 minutes more. In all, the paper had 536 sentences by the end of today. How many sentences did she start with today?"""
    sentences_per_minute = 6
    minutes_typed = 20 + 15 + 18
    sentences_erased = 40
    total_sentences = 536
    sentences_started = total_sentences - sentences_erased
    result = sentences_started
    return result

print(solution())