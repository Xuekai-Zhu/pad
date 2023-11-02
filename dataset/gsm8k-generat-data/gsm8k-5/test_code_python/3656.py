def solution():
    hand_crank_speed = 1 / 45  # The hand-crank sharpener can sharpen 1 pencil every 45 seconds
    electric_speed = 1 / 20  # The electric sharpener can sharpen 1 pencil every 20 seconds

    # Calculate the total number of pencils the hand-crank sharpener can sharpen in 6 minutes
    hand_crank_pencils = 6 * 60 * hand_crank_speed

    # Calculate the total number of pencils the electric sharpener can sharpen in 6 minutes
    electric_pencils = 6 * 60 * electric_speed

    # Calculate the difference in the number of pencils sharpened
    difference = electric_pencils - hand_crank_pencils
    result = difference
    return result

print(solution())