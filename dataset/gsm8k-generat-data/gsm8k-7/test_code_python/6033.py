def solution():
    first_gen_tail_length = 16
    tail_length_increase = 0.25  # 25% increase per generation

    # Calculate the length of the second generation's tails
    second_gen_tail_length = first_gen_tail_length * (1 + tail_length_increase)

    # Calculate the length of the third generation's tails
    third_gen_tail_length = second_gen_tail_length * (1 + tail_length_increase)

    result = third_gen_tail_length
    return result

print(solution())