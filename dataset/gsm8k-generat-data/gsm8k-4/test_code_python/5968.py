def solution():
    """Josue planted a tree in his backyard that grows at the rate of 2 feet per week. If the tree is currently 10 feet tall, what would be the tree's total height after 4 months (assuming each month is 4 weeks long)?"""
    # Define the initial height of the tree and the growth rate in feet per week
    initial_height = 10
    growth_rate = 2

    # Define the number of weeks in 4 months
    weeks_in_4_months = 16

    # Calculate the total growth in height over 16 weeks
    total_growth = growth_rate * weeks_in_4_months

    # Calculate the final height of the tree
    final_height = initial_height + total_growth

    result = final_height
    return result

print(solution())