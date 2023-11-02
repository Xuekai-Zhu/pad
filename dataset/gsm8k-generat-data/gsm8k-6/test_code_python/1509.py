def solution():
    # Calculate John's new height in inches after the growth spurt
    height_inches = 66 + 2*3  # John grew 2 inches per month for 3 months

    # Convert the height to feet and round to 2 decimal places
    height_feet = round(height_inches/12, 2)

    result = height_feet
    return result

print(solution())