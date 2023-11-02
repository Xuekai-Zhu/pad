def solution():
    """Malcolm brushes his teeth for 2 minutes after breakfast, lunch and dinner. After 30 days, how many hours does he spend brushing his teeth?"""
    # Define the number of times Malcolm brushes his teeth per day
    brushes_per_day = 3

    # Define the length of time Malcolm brushes his teeth each time
    brush_time = 2 # in minutes

    # Calculate the total number of minutes Malcolm spends brushing his teeth per day
    daily_minutes = brushes_per_day * brush_time

    # Calculate the total number of minutes Malcolm spends brushing his teeth over 30 days
    total_minutes = daily_minutes * 30

    # Convert the total number of minutes to hours
    total_hours = total_minutes / 60

    # Display the total number of hours Malcolm spends brushing his teeth over 30 days
    result = total_hours
    return result

print(solution())