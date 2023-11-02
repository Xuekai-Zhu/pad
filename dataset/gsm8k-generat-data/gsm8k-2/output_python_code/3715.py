def solution():
    """John starts at an elevation of 400 feet. He travels downward at a rate of 10 feet down per minute for 5 minutes. What is his elevation now?"""
    starting_elevation = 400
    rate = 10
    time = 5
    final_elevation = starting_elevation - (rate * time)
    result = final_elevation
    return result

print(solution())