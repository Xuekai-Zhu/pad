def solution():
    """Iggy is training for a marathon. On Monday, he runs 3 miles. On Tuesday, he runs 4 miles. On Wednesday, he runs 6 miles. On Thursday, he runs 8 miles. On Friday, he runs 3 miles. Iggy runs at a pace of 1 mile in 10 minutes. What is the total number of hours that Iggy spends running from Monday to Friday?"""
    # Define Iggy's running pace
    PACE = 10 # minutes per mile

    # Calculate the total distance Iggy runs
    total_distance = 3 + 4 + 6 + 8 + 3 # miles

    # Calculate the total time Iggy spends running in minutes
    total_time_minutes = total_distance * PACE

    # Convert the total time to hours and minutes
    total_time_hours = total_time_minutes / 60
    total_time_minutes %= 60

    # Display the total time Iggy spends running
    result = f"{int(total_time_hours)} hours and {total_time_minutes} minutes"
    return result

print(solution())