def solution():
    # Calculate the number of pencils sharpened by hand-crank sharpener in 6 minutes
    hand_crank_time_sec = 45  # time taken to sharpen one pencil in seconds
    hand_crank_pencils = 6*60 // hand_crank_time_sec  # 6 minutes converted to seconds
    # Calculate the number of pencils sharpened by electric sharpener in 6 minutes
    electric_time_sec = 20  # time taken to sharpen one pencil in seconds
    electric_pencils = 6*60 // electric_time_sec  # 6 minutes converted to seconds
    # Calculate the difference in pencils sharpened by the two sharpeners
    difference = electric_pencils - hand_crank_pencils
    result = difference
    return result

print(solution())