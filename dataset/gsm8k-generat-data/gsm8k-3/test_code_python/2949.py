def solution():
    """The Parker family needs to leave the house by 5 pm for a dinner party. Mrs. Parker was waiting to get into the bathroom at 2:30 pm. Her oldest daughter used the bathroom for 45 minutes and her youngest daughter used the bathroom for another 30 minutes. Then her husband used it for 20 minutes. How much time will Mrs. Parker have to use the bathroom to leave on time?"""
    # Convert the given times into minutes after 2:30 pm
    daughter1_time = 45
    daughter2_time = 30
    husband_time = 20
    total_used_time = daughter1_time + daughter2_time + husband_time

    # Calculate the remaining time until 5 pm in minutes
    remaining_time = (5 - 2.5) * 60

    # Calculate the available time for Mrs. Parker to use the bathroom
    available_time = remaining_time - total_used_time

    # Convert the available time back to hours and minutes
    remaining_hours = available_time // 60
    remaining_minutes = available_time % 60

    # Display the available time for Mrs. Parker to use the bathroom
    result = f'{remaining_hours} hours and {remaining_minutes} minutes'
    return result

print(solution())