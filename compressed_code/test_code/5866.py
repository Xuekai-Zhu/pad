def solution():
    
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