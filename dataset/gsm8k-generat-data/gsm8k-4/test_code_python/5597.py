def solution():
    """Jasmine gets off of work at 4:00 pm.  After that, it will take her 30 minutes to commute home, 30 minutes to grocery shop, 10 minutes to pick up the dry cleaning, 20 minutes to pick up the dog from the
    groomers and 90 minutes to cook dinner when she returns home.  What time will she eat dinner?"""
    
    # Convert the starting time into minutes
    start_time = 4 * 60

    # Calculate the total time needed for all tasks
    total_time = 30 + 30 + 10 + 20 + 90

    # Add the total time to the starting time
    end_time = start_time + total_time

    # Format the end time into hours and minutes
    end_hour = end_time // 60
    end_minute = end_time % 60

    # Return the formatted end time
    result = f"{end_hour}:{end_minute:02}"
    return result

print(solution())