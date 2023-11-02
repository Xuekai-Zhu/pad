def solution():
    """Larry spends half an hour twice a day walking and playing with his dog. He also spends a fifth of an hour every day feeding his dog. How many minutes does Larry spend on his dog each day?"""
    # Define the time in hours for walking/playing and feeding
    time_walkplay = 0.5
    time_feed = 1/5

    # Convert the time in hours to minutes and calculate the total time spent with the dog each day
    total_time = (time_walkplay * 2 + time_feed) * 60

    # Return the total time in minutes
    result = total_time
    return result

print(solution())