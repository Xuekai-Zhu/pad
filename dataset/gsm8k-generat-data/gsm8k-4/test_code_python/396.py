def solution():
    """Holly needs to take 2 insulin pills per day, 3 blood pressure pills per day, and twice as many anticonvulsants as blood pressure pills each day. How many pills does Holly take in a week?"""
    # Define the number of pills needed per day
    insulin = 2
    bp = 3
    anticonvulsant = 2 * bp

    # Calculate the total number of pills needed per week
    pills_per_day = insulin + bp + anticonvulsant
    pills_per_week = pills_per_day * 7

    # return the result
    result = pills_per_week
    return result

print(solution())