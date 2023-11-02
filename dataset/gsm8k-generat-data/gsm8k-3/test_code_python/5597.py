def solution():
    """Jasmine gets off of work at 4:00 pm.  After that, it will take her 30 minutes to commute home, 30 minutes to grocery shop, 10 minutes to pick up the dry cleaning, 20 minutes to pick up the dog from the groomers and 90 minutes to cook dinner when she returns home.  What time will she eat dinner?"""
    # Define the time Jasmine gets off work
    off_work_time = 4 * 60  # 4:00 pm

    # Calculate the total time for errands and cooking
    total_time = 30 + 30 + 10 + 20 + 90

    # Calculate the dinner time in minutes
    dinner_time = off_work_time + total_time

    # Convert the dinner time to hours and minutes
    hours = dinner_time // 60
    minutes = dinner_time % 60

    # Display the dinner time
    result = f"{hours:02}:{minutes:02}"
    return result

print(solution())