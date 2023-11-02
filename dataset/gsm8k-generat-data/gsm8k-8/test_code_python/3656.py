def solution():
    # Define the time it takes for each sharpener to sharpen one pencil
    hand_crank_time = 45
    electric_time = 20

    # Calculate how many pencils each sharpener can sharpen in 6 minutes (360 seconds)
    hand_crank_pencils = (360 // hand_crank_time)
    electric_pencils = (360 // electric_time)

    # Calculate the difference in the number of pencils sharpened by each sharpener in 6 minutes
    pencil_difference = electric_pencils - hand_crank_pencils

    result = pencil_difference
    return result

print(solution())