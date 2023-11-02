def solution():
    """Jack needs to mop the bathroom and the kitchen. If the bathroom floor is 24 square feet and the kitchen floor is 80 square feet, and Jack can mop 8 square feet per minute, how many minutes does he spend mopping?"""
    # Define the floor areas
    bathroom_area = 24
    kitchen_area = 80

    # Calculate the total area to mop
    total_area = bathroom_area + kitchen_area

    # Calculate the time to mop the total area
    time = total_area / 8

    # Return the result
    result = time
    return result

print(solution())