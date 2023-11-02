def solution():
    """James is trying to create a new breed of kittens with extra-long tails. Each generation of kittens he breeds has a tail 25% longer than the last generation. If the first generation has tails 16 cm long, how long are the third generation's tails?"""
    first_generation_tail_length = 16
    second_generation_tail_length = first_generation_tail_length * 1.25
    third_generation_tail_length = second_generation_tail_length * 1.25
    result = third_generation_tail_length
    return result

print(solution())