def solution():
    """Jordan decides to start an exercise program when he weighs 250 pounds. For the first 4 weeks, he loses 3 pounds a week. After that, he loses 2 pounds a week for 8 weeks. How much does Jordan now weigh?"""
    starting_weight = 250
    first_month_loss = 3 * 4
    remaining_loss = 2 * 8
    current_weight = starting_weight - first_month_loss - remaining_loss
    result = current_weight
    return result

print(solution())