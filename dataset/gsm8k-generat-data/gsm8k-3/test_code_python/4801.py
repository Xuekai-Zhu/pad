def solution():
    """Tom decides to start running 5 days a week to lose weight.  He runs 1.5 hours each day.  He runs at a speed of 8 mph.  How many miles does he run a week?"""
    # Define the number of days Tom runs and the time he spends running each day
    NUM_DAYS = 5
    RUN_TIME = 1.5

    # Define Tom's running speed
    SPEED = 8

    # Calculate the total distance Tom runs each day
    distance = SPEED * RUN_TIME

    # Calculate the total distance Tom runs in a week
    total_distance = distance * NUM_DAYS

    # Display the total distance Tom runs in miles
    result = total_distance
    return result

print(solution())