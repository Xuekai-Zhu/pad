def solution():
    """The Parker family needs to leave the house by 5 pm for a dinner party. Mrs. Parker was waiting to get into the bathroom at 2:30 pm. Her oldest daughter used the bathroom for 45 minutes and her youngest daughter used the bathroom for another 30 minutes. Then her husband used it for 20 minutes. How much time will Mrs. Parker have to use the bathroom to leave on time?"""
    # Define the time when the family needs to leave the house
    LEAVE_TIME = "5:00 pm"

    # Define the time when Mrs. Parker started waiting for the bathroom
    START_TIME = "2:30 pm"

    # Define the time used by each family member in the bathroom
    DAUGHTER_1_TIME = 45
    DAUGHTER_2_TIME = 30
    HUSBAND_TIME = 20

    # Calculate the total time used by the family in the bathroom
    total_bathroom_time = DAUGHTER_1_TIME + DAUGHTER_2_TIME + HUSBAND_TIME

    # Convert the start time and leave time to datetime objects
    start_time_obj = datetime.datetime.strptime(START_TIME, "%I:%M %p")
    leave_time_obj = datetime.datetime.strptime(LEAVE_TIME, "%I:%M %p")

    # Subtract the total bathroom time from the time remaining until the family needs to leave
    time_left = leave_time_obj - start_time_obj - datetime.timedelta(minutes=total_bathroom_time)

    # Convert the remaining time to minutes
    minutes_left = int(time_left.total_seconds() / 60)

    # Return the result
    result = minutes_left
    return result

print(solution())