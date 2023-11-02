def solution():
    """A hand-crank pencil sharpener can sharpen one pencil every forty-five seconds. An electric version can sharpen one in twenty seconds. How many more pencils can the electric sharpener sharpen than the hand-crank sharpener in six minutes?"""
    # Define the time it takes to sharpen one pencil for each sharpener
    HAND_CRANK_TIME = 45
    ELECTRIC_TIME = 20

    # Calculate the number of pencils each sharpener can sharpen in six minutes
    hand_crank_pencils = (6 * 60) // HAND_CRANK_TIME # round down to nearest integer
    electric_pencils = (6 * 60) // ELECTRIC_TIME # round down to nearest integer

    # Calculate the difference in the number of pencils sharpened by each sharpener
    difference = electric_pencils - hand_crank_pencils

    # Display the difference in the number of pencils sharpened
    result = difference
    return result

print(solution())