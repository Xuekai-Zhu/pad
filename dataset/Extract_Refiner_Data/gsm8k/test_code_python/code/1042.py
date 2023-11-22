def solution():
    
    # Define the number of painters and the daily worked time
    num_painters = 4
    daily_time = 3/8

    # Calculate the total time worked in a week
    weekly_time = num_painters * daily_time * 7

    # Calculate the total time worked in 3 weeks
    total_time = weekly_time * 3

    # Calculate the hours worked per painter
    hours_per_painter = total_time / num_painters

    # Display the hours worked per painter
    result = hours_per_painter
    return result

print(solution())