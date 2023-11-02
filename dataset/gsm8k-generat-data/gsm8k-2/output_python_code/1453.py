def solution():
    """Tom decides to lease a car. He drives 50 miles on Monday, Wednesday, and Friday, and Sunday, For the rest of the days, he drives 100 miles. He has to pay $.1 per mile he drives. He also has to pay a weekly fee of $100. How much does he have to pay in a year?"""
    weekly_fee = 100
    cost_per_mile = 0.1
    miles_per_week = (50 * 3) + (100 * 4)
    miles_per_year = miles_per_week * 52
    total_cost = (miles_per_year * cost_per_mile) + (weekly_fee * 52)
    result = total_cost
    return result

print(solution())