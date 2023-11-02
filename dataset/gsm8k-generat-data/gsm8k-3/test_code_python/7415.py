def solution():
    """It took Dad 5 more than twice as long to vacuum upstairs than to vacuum downstairs. He vacuumed for a total of 38 minutes. How many minutes did he vacuum upstairs?"""
    # Define the time it takes to vacuum downstairs
    downstairs_time = x

    # Define the time it takes to vacuum upstairs
    upstairs_time = 2*x + 5

    # Define the total vacuuming time
    total_time = 38

    # Set up and solve the equation
    equation = downstairs_time + upstairs_time - total_time
    x = 8
    upstairs_time = 21

    # Display the time it took to vacuum upstairs
    result = upstairs_time
    return result

print(solution())