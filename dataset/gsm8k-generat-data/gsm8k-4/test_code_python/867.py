def solution():
    """Bob runs 6 miles per hour. His friend Jim runs at 9 miles per hour. If Bob has a 1 mile head-start, how many minutes will it take before Jim catches him?"""
    # Define the speeds of Bob and Jim
    bob_speed = 6
    jim_speed = 9

    # Define the head start distance in miles
    head_start_distance = 1

    # Calculate the relative speed of Jim to Bob
    relative_speed = jim_speed - bob_speed

    # Calculate the time it takes Jim to catch up to Bob in hours
    time_in_hours = head_start_distance / relative_speed

    # Convert the time to minutes
    time_in_minutes = time_in_hours * 60

    result = round(time_in_minutes)
    return result

print(solution())