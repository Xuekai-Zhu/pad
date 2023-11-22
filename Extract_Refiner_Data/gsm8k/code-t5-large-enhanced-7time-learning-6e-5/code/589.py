def solution():
    
    # Define the initial height of the window and the height increase per day
    initial_height = 20
    height_increase_per_day = 2

    # Define the height of the beanstalk
    beanstalk_height = 4

    # Initialize the day counter and the current height
    days = 0
    current_height = initial_height

    # Loop until the height is taller than Mark's window
    while current_height < beanstalk_height:
        # Increment the day counter
        days += 1

        # Double the height every day
        current_height *= height_increase_per_day

    # Display the number of days it took to reach the second-story window
    result = days
    return result

print(solution())