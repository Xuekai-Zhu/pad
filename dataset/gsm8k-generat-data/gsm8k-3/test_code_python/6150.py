def solution():
    """Manny has a tree that grows at the rate of fifty centimeters every two weeks. If the tree is currently 2 meters tall, how tall, in centimeters, will the tree be in 4 months?"""
    # Define the growth rate of the tree in centimeters per week
    GROWTH_RATE = 25

    # Convert the initial height of the tree to centimeters
    height = 2 * 100

    # Calculate the total growth of the tree over 4 months
    total_growth = GROWTH_RATE * 4 * 4

    # Calculate the final height of the tree in centimeters
    final_height = height + total_growth

    # Display the final height of the tree in centimeters
    result = final_height
    return result

print(solution())