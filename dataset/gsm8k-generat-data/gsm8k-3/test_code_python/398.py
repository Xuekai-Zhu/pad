def solution():
    """Holly needs to take 2 insulin pills per day, 3 blood pressure pills per day, and twice as many anticonvulsants as blood pressure pills each day. How many pills does Holly take in a week?"""
    # Define the number of pills per day for each type of medication
    INSULIN = 2
    BLOOD_PRESSURE = 3
    ANTICONVULSANT = BLOOD_PRESSURE * 2

    # Calculate the total number of pills Holly takes in a day and in a week
    pills_per_day = INSULIN + BLOOD_PRESSURE + ANTICONVULSANT
    pills_per_week = pills_per_day * 7

    # Display the total number of pills Holly takes in a week
    result = pills_per_week
    return result

print(solution())