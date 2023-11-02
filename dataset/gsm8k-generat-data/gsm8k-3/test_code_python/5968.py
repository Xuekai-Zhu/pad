def solution():
    """Josue planted a tree in his backyard that grows at the rate of 2 feet per week. If the tree is currently 10 feet tall, what would be the tree's total height after 4 months (assuming each month is 4 weeks long)?"""
    # Define the growth rate of the tree
    GROWTH_RATE = 2

    # Calculate the total growth of the tree after 4 months (16 weeks)
    total_growth = GROWTH_RATE * 16

    # Calculate the total height of the tree after 4 months
    total_height = 10 + total_growth

    # Display the total height of the tree
    result = total_height
    return result

print(solution())