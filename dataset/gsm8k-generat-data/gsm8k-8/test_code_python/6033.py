def solution():
    # Define the length of the first generation's tails
    first_gen_tail_length = 16

    # Calculate the length of the second generation's tails
    second_gen_tail_length = first_gen_tail_length * 1.25

    # Calculate the length of the third generation's tails
    third_gen_tail_length = second_gen_tail_length * 1.25

    result = third_gen_tail_length
    return result

print(solution())