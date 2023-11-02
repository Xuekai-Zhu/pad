def solution():
    """Gary manages two Amazon distribution centers. The first center processes 10000 packages per day, and the second center processes three times that volume. If Amazon makes 5 cents of profit per package, how much profit per week do the two centers make combined?"""
    # Define the number of packages processed by the first center
    center1_packages = 10000

    # Define the number of packages processed by the second center (3 times the first center)
    center2_packages = center1_packages * 3

    # Calculate the total number of packages processed per week
    total_packages = (center1_packages + center2_packages) * 7

    # Calculate the total profit from all the packages
    total_profit = total_packages * 0.05

    # Return the result
    result = total_profit
    return result

print(solution())