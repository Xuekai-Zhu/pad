def solution():
    
    third_segment = 10
    second_segment = third_segment * 2
    first_segment = (second_segment + third_segment) * 2
    total_length = first_segment + second_segment + third_segment
    result = total_length
    return result

print(solution())