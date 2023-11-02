def solution():
    
    tape_strands = 22
    hannah_rate = 8
    son_rate = 3
    total_rate = hannah_rate + son_rate
    time_to_free = tape_strands / total_rate
    result = time_to_free
    return result

print(solution())