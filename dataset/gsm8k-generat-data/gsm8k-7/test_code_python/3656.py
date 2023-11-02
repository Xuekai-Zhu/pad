def solution():
    hand_crank_time_per_pencil = 45  # in seconds
    electric_time_per_pencil = 20  # in seconds
    time_limit = 6 * 60  # in seconds

    # Calculate the number of pencils the hand-crank sharpener can sharpen in the time limit
    hand_crank_num_pencils = time_limit // hand_crank_time_per_pencil

    # Calculate the number of pencils the electric sharpener can sharpen in the time limit
    electric_num_pencils = time_limit // electric_time_per_pencil

    # Calculate the difference in the number of pencils sharpened
    num_pencils_difference = electric_num_pencils - hand_crank_num_pencils
    result = num_pencils_difference
    return result

print(solution())