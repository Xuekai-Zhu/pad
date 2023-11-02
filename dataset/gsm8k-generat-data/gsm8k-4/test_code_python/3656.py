def solution():
    """A hand-crank pencil sharpener can sharpen one pencil every forty-five seconds. An electric version can sharpen one in twenty seconds. How many more pencils can the electric sharpener sharpen than the hand-crank sharpener in six minutes?"""
    # Define the time to sharpen one pencil for each sharpener
    hand_crank_time = 45
    electric_time = 20

    # Calculate the number of pencils each sharpener can sharpen in 6 minutes
    hand_crank_pencils = (6 * 60) // hand_crank_time
    electric_pencils = (6 * 60) // electric_time

    # Calculate the difference in the number of pencils sharpened by each sharpener
    pencil_difference = electric_pencils - hand_crank_pencils

    # return the result
    result = pencil_difference
    return result

print(solution())