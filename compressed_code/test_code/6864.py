def solution():
    
    strands_to_cut = 22
    hannah_rate = 8
    son_rate = 3
    total_rate = hannah_rate + son_rate
    time_to_free = strands_to_cut / total_rate
    result = time_to_free
    return result

print(solution())