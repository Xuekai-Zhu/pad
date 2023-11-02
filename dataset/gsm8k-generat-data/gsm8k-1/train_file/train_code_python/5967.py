def solution():
    """Josue planted a tree in his backyard that grows at the rate of 2 feet per week. If the tree is currently 10 feet tall, what would be the tree's total height after 4 months (assuming each month is 4 weeks long)?"""
    current_height = 10
    growth_rate = 2 * 4 # 2 feet per week times 4 weeks per month
    total_growth = growth_rate * 4 # 4 months
    total_height = current_height + total_growth
    result = total_height
    return result

print(solution())