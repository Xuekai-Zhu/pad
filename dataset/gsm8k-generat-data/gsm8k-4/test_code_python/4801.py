def solution():
    """Tom decides to start running 5 days a week to lose weight. He runs 1.5 hours each day. He runs at a speed of 8 mph. How many miles does he run a week?"""
    # Define the number of days Tom runs
    days = 5

    # Define the time Tom runs each day, in hours
    time_per_day = 1.5

    # Define Tom's running speed in miles per hour
    speed = 8

    # Calculate the total distance Tom runs each day
    distance_per_day = speed * time_per_day

    # Calculate the total distance Tom runs in a week
    distance_per_week = distance_per_day * days

    # return the result
    result = distance_per_week
    return result

print(solution())