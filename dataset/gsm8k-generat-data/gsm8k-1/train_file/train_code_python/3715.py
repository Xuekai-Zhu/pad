def solution():
    """John starts at an elevation of 400 feet. He travels downward at a rate of 10 feet down per minute for 5 minutes. What is his elevation now?"""
    starting_elevation = 400
    rate_of_descent = 10
    time_of_descent = 5
    new_elevation = starting_elevation - (rate_of_descent * time_of_descent)
    result = new_elevation
    return result

print(solution())