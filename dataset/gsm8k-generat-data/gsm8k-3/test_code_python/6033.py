def solution():
    """James is trying to create a new breed of kittens with extra-long tails. Each generation of kittens he breeds has a tail 25% longer than the last generation. If the first generation has tails 16 cm long, how long are the third generation's tails?"""
    # Define the length of the first generation's tails
    first_gen_length = 16

    # Calculate the length of the second generation's tails
    second_gen_length = first_gen_length * 1.25

    # Calculate the length of the third generation's tails
    third_gen_length = second_gen_length * 1.25

    # Display the length of the third generation's tails
    result = third_gen_length
    return result

print(solution())