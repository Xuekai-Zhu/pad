def solution():
    # Define the variables
    crickets_per_week_at_90 = 4
    crickets_per_week_at_100 = 8
    weeks_at_90 = 0.8 * 15
    weeks_at_100 = 0.2 * 15

    # Calculate the total number of crickets eaten
    total_crickets = (crickets_per_week_at_90 * weeks_at_90) + (crickets_per_week_at_100 * weeks_at_100)

    result = total_crickets
    return result

print(solution())