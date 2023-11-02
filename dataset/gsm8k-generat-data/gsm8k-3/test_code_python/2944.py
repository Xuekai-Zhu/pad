def solution():
    """Jane runs 3 kilometers in two hours. What is her speed in meters per minute?"""
    # Convert kilometers to meters and hours to minutes
    distance = 3000 # 3 kilometers = 3000 meters
    time = 120 # 2 hours = 120 minutes

    # Calculate her speed in meters per minute
    speed = distance / time

    # Display her speed in meters per minute
    result = speed
    return result

print(solution())