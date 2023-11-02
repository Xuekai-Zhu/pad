def solution():
    """Gilbert, the bearded dragon, eats 4 crickets per week when the temperature averages 90 degrees F per day, but he eats twice as many crickets per week when the temperature averages 100 degrees F. How many crickets will he eat over 15 weeks if the temperature averages 90 degrees F for 80% of the time, and 100 degrees F for the remainder of the time?"""
    temp_90_avg_weeks = 15 * 0.8
    temp_100_avg_weeks = 15 * 0.2
    crickets_per_week_at_90_degrees = 4
    crickets_per_week_at_100_degrees = 8
    total_crickets = (crickets_per_week_at_90_degrees * temp_90_avg_weeks) + \
                    (crickets_per_week_at_100_degrees * temp_100_avg_weeks)
    result = total_crickets
    return result

print(solution())