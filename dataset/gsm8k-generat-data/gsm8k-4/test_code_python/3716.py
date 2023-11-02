def solution():
    """John starts at an elevation of 400 feet. He travels downward at a rate of 10 feet down per minute for 5 minutes. What is his elevation now?"""
    # Define the starting elevation and the rate of descent
    starting_elevation = 400
    descent_rate = 10

    # Calculate the new elevation after 5 minutes of descent
    new_elevation = starting_elevation - (descent_rate * 5)

    # Return the result
    result = new_elevation
    return result

print(solution())