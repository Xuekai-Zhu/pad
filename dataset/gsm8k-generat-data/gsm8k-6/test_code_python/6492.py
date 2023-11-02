def solution():
    # Calculate the number of worms eaten by 3 crows in 1 hour
    worms_per_hour = 30/3

    # Calculate the number of worms eaten by 5 crows in 2 hours
    worms_in_2_hours = worms_per_hour * 5 * 2
    result = worms_in_2_hours
    return result

print(solution())