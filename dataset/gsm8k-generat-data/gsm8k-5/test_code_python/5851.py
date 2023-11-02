def solution():
    crickets_90_degrees = 4  # Gilbert eats 4 crickets per week when temperature averages 90 degrees
    crickets_100_degrees = 2 * crickets_90_degrees  # Gilbert eats twice as many crickets when temperature averages 100 degrees
    weeks = 15  # Gilbert needs to determine how many crickets he will eat over 15 weeks

    # Calculate the total number of crickets Gilbert eats when temperature averages 90 degrees
    total_crickets_90 = (0.8 * 90 * crickets_90_degrees) * weeks

    # Calculate the total number of crickets Gilbert eats when temperature averages 100 degrees
    total_crickets_100 = (0.2 * 100 * crickets_100_degrees) * weeks

    # Calculate the total number of crickets Gilbert eats over 15 weeks
    total_crickets = total_crickets_90 + total_crickets_100
    result = total_crickets
    return result

print(solution())