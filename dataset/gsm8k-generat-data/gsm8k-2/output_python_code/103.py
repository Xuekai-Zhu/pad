def solution():
    """Janice can type 6 sentences per minute. Today at work, Janice continued working on a paper she started typing yesterday. She typed for 20 minutes, took a break, and typed 15 minutes longer. She then had to erase 40 sentences she had typed incorrectly. After a meeting, she typed for 18 minutes more. In all, the paper had 536 sentences by the end of today. How many sentences did she start with today?"""
    typing_speed = 6
    morning_typing_time = 20
    afternoon_typing_time = 15
    erasing_time = 0
    meeting_typing_time = 18
    total_typing_time = morning_typing_time + afternoon_typing_time + meeting_typing_time
    total_typing = total_typing_time * typing_speed
    total_sentences = total_typing - erasing_time
    initial_sentences = total_sentences - 536
    result = initial_sentences
    return result

print(solution())