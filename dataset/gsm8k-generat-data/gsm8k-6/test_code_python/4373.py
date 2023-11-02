def solution():
    # Calculate the total number of weeds pulled by Lucille
    total_weeds = 11 + 14 + (1/2)*32  # Lucille weeded half the grass around the fruit trees

    # Calculate Lucille's earnings
    earnings = 6 * total_weeds

    # Calculate how many cents Lucille has left after buying a soda for 99 cents
    left_over = earnings - 99

    result = left_over
    return result

print(solution())