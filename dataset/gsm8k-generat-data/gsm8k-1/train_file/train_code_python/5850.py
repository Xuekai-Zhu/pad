def solution():
    """Gilbert, the bearded dragon, eats 4 crickets per week when the temperature averages 90 degrees F per day, but he eats twice as many crickets per week when the temperature averages 100 degrees F. How many crickets will he eat over 15 weeks if the temperature averages 90 degrees F for 80% of the time, and 100 degrees F for the remainder of the time?"""
    crickets_per_week_at_90 = 4
    crickets_per_week_at_100 = crickets_per_week_at_90 * 2
    weeks_at_90_degrees = 15 * 0.8
    weeks_at_100_degrees = 15 * 0.2
    total_crickets = (crickets_per_week_at_90 * weeks_at_90_degrees) + (crickets_per_week_at_100 * weeks_at_100_degrees)
    result = total_crickets
    return result

print(solution())