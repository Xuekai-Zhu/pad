def solution():
    """Iggy is training for a marathon. On Monday, he runs 3 miles. On Tuesday, he runs 4 miles. On Wednesday, he runs 6 miles. On Thursday, he runs 8 miles. On Friday, he runs 3 miles. Iggy runs at a pace of 1 mile in 10 minutes. What is the total number of hours that Iggy spends running from Monday to Friday?"""
    # Define the pace of Iggy's running
    PACE = 10  # in minutes per mile

    # Define the distances run each day
    monday_distance = 3
    tuesday_distance = 4
    wednesday_distance = 6
    thursday_distance = 8
    friday_distance = 3

    # Calculate the total distance run
    total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance + friday_distance

    # Calculate the total time spent running in minutes
    total_time_minutes = total_distance * PACE

    # Convert the total time to hours
    total_time_hours = total_time_minutes / 60

    # Return the result
    result = total_time_hours
    return result

print(solution())