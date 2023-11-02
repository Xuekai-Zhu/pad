def solution():
    """William left Missouri by 7:00 AM and arrived at his hometown by 8:00 PM. He had 3 stops of 25, 10 and 25 minutes respectively during the journey. How many hours did he spend on the road?"""
    # Define the start and end times of the journey
    start_time = 7 * 60  # convert to minutes
    end_time = 20 * 60  # convert to minutes

    # Calculate the total duration of the journey
    total_duration = end_time - start_time

    # Subtract the duration of the stops from the total duration
    total_duration -= (25 + 10 + 25)  # in minutes

    # Convert the duration to hours and minutes
    hours = total_duration // 60
    minutes = total_duration % 60

    # Display the duration in hours and minutes
    result = f"{hours} hours and {minutes} minutes"
    return result

print(solution())