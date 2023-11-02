def solution():
    """Making an equal number of drums of paint each day, a paint mixer takes three days to make 18 drums of paint. How many days will it take for him to make 360 drums of paint?"""
    # Calculate the number of drums of paint the mixer can make in one day
    drums_per_day = 18 / 3

    # Calculate the number of days it will take to make 360 drums of paint
    num_days = 360 / drums_per_day

    # Display the number of days
    result = num_days
    return result

print(solution())