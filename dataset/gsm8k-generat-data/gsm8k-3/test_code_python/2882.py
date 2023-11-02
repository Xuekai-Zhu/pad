def solution():
    """Dexter and Jay are using a gallon of white paint to paint the walls. Dexter used 3/8 of the gallon of paint while Jay used 5/8 of a gallon of paint. If a gallon is equal to 4 liters, how many liters of paint were left from Dexter and Jay combined?"""
    # Define the total amount of paint used
    total_paint_used = (3/8 + 5/8) * 4

    # Calculate the amount of paint left
    paint_left = 4 - total_paint_used

    # Display the amount of paint left
    result = paint_left
    return result

print(solution())