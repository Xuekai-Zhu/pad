def solution():
    """Larry spends half an hour twice a day walking and playing with his dog. He also spends a fifth of an hour every day feeding his dog. How many minutes does Larry spend on his dog each day?"""
    # Define the time (in hours) Larry spends walking and playing with his dog, and feeding his dog
    walking_time = 0.5
    feeding_time = 0.2

    # Calculate the total time (in hours) Larry spends on his dog each day
    total_time = walking_time * 2 + feeding_time

    # Convert the total time to minutes
    total_time_minutes = total_time * 60

    # Return the result
    result = total_time_minutes
    return result

print(solution())