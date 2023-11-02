def solution():
    """Kelly puts string cheeses in her kids lunches 5 days per week. Her oldest wants 2 every day and her youngest will only eat 1. The packages come with 30 string cheeses per pack. How many packages of string cheese will Kelly need to fill her kids lunches for 4 weeks?"""
    days_per_week = 5
    oldest_child_cheeses = 2
    youngest_child_cheeses = 1
    total_lunches_per_week = (oldest_child_cheeses + youngest_child_cheeses) * days_per_week
    packages_needed_per_week = total_lunches_per_week / 30
    packages_needed_per_month = packages_needed_per_week * 4
    result = packages_needed_per_month
    return result

print(solution())