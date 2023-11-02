def solution():
    """John was 66 inches tall.  He had a growth spurt and grew 2 inches per month for 3 months.  How tall is he in feet?"""
    # Define John's initial height in inches
    initial_height = 66

    # Calculate John's final height in inches
    final_height = initial_height + (2 * 3)

    # Convert John's final height from inches to feet
    height_feet = final_height / 12

    # Display John's height in feet
    result = height_feet
    return result

print(solution())