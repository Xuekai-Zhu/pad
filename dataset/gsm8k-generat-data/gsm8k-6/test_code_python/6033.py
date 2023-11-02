def solution():
    # Calculate the length of tails in the third generation of kittens
    first_gen_tails = 16
    second_gen_tails = first_gen_tails * 1.25  # 25% longer than the first generation
    third_gen_tails = second_gen_tails * 1.25  # 25% longer than the second generation
    result = third_gen_tails
    return result

print(solution())