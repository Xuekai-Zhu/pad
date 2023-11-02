def solution():
    
    first_generation_tail_length = 16
    second_generation_tail_length = first_generation_tail_length * 1.25
    third_generation_tail_length = second_generation_tail_length * 1.25
    result = third_generation_tail_length
    return result

print(solution())