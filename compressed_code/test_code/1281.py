def solution():
    
    total_chapters = 8
    chapters_read = 2
    time_taken = 3
    chapters_remaining = total_chapters - chapters_read
    time_per_chapter = time_taken / chapters_read
    time_to_finish = time_per_chapter * chapters_remaining
    result = time_to_finish
    return result

print(solution())