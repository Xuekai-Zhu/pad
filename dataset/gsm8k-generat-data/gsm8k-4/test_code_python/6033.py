def solution():
    """James is trying to create a new breed of kittens with extra-long tails. Each generation of kittens he breeds has a tail 25% longer than the last generation. If the first generation has tails 16 cm long, how long are the third generation's tails?"""
    # Define the initial tail length and the growth factor
    INITIAL_TAIL_LENGTH = 16
    GROWTH_FACTOR = 1.25

    # Calculate the tail length of the third generation
    third_gen_tail_length = INITIAL_TAIL_LENGTH * GROWTH_FACTOR * GROWTH_FACTOR

    result = round(third_gen_tail_length, 2)
    return result

print(solution())