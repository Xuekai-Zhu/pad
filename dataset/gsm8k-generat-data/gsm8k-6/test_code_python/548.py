def solution():
    # Calculate the total number of packages processed per week by both centers
    total_packages_per_week = (10000 * 7) + (3 * 10000 * 7)  # first center processes 10000 packages per day, second center processes three times that volume; both centers operate for 7 days a week.

    # Calculate the total profit per week earned by both centers
    total_profit_per_week = total_packages_per_week * 0.05  # Amazon makes 5 cents of profit per package
    
    result = total_profit_per_week
    return result

print(solution())