def solution():
    """Kelly puts string cheeses in her kids lunches 5 days per week. Her oldest wants 2 every day and her youngest will only eat 1. The packages come with 30 string cheeses per pack. How many packages of string cheese will Kelly need to fill her kids lunches for 4 weeks?"""
    days_per_week = 5
    total_days = 4 * 7
    oldest_child_cheese = 2
    youngest_child_cheese = 1
    total_cheese_per_day = oldest_child_cheese + youngest_child_cheese
    total_cheese_needed = days_per_week * total_cheese_per_day
    packages_needed = (total_cheese_needed * total_days) / 30
    result = math.ceil(packages_needed)
    return result

print(solution())