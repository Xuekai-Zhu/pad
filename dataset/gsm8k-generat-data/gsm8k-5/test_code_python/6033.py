def solution():
    first_gen_tail_length = 16  # The first generation has a tail length of 16 cm
    second_gen_tail_length = first_gen_tail_length * 1.25  # The second generation's tails are 25% longer than the first generation's
    third_gen_tail_length = second_gen_tail_length * 1.25  # The third generation's tails are 25% longer than the second generation's

    result = third_gen_tail_length
    return result

print(solution())