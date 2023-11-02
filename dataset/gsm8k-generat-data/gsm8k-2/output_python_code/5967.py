def solution():
    """Josue planted a tree in his backyard that grows at the rate of 2 feet per week. If the tree is currently 10 feet tall, what would be the tree's total height after 4 months (assuming each month is 4 weeks long)?"""
    growth_per_week = 2
    initial_height = 10
    weeks_in_4_months = 4 * 4
    total_growth = growth_per_week * weeks_in_4_months
    total_height = initial_height + total_growth
    result = total_height
    return result

print(solution())