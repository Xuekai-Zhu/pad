def solution():
    """John was 66 inches tall. He had a growth spurt and grew 2 inches per month for 3 months. How tall is he in feet?"""
    # Define John's starting height in inches
    starting_height = 66

    # Calculate John's height after growing for 3 months
    final_height = starting_height + (2 * 3)

    # Convert John's final height from inches to feet
    final_height_feet = final_height / 12

    result = final_height_feet
    return result

print(solution())