def solution():
    first_center_volume = 10000  # The first center processes 10000 packages per day
    second_center_volume = 3 * first_center_volume  # The second center processes three times the volume of the first center
    packages_per_week = (first_center_volume + second_center_volume) * 7  # Total number of packages processed per week
    profit_per_package = 0.05  # Amazon makes 5 cents of profit per package

    # Calculate the total profit per week
    total_profit = packages_per_week * profit_per_package
    result = total_profit
    return result

print(solution())