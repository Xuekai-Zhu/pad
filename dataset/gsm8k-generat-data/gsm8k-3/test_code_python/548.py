def solution():
    """Gary manages two Amazon distribution centers. The first center processes 10000 packages per day, and the second center processes three times that volume. If Amazon makes 5 cents of profit per package, how much profit per week do the two centers make combined?"""
    # Define variables
    center1_packages = 10000
    center2_packages = 3 * center1_packages
    profit_per_package = 0.05
    
    # Calculate the total packages processed in a week
    total_packages = (center1_packages + center2_packages) * 7
    
    # Calculate the profit for the week
    total_profit = total_packages * profit_per_package
    
    result = total_profit
    return result

print(solution())