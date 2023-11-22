def solution():
    
    # Define the distance John runs in a week
    distance = 60

    # Define the number of days John runs in a week
    days = 3

    # Calculate the total distance John runs in a week
    total_distance = distance * days

    # Calculate the distance John runs in the first day
    first_day_distance = distance + 3

    # Calculate the distance John runs in the other two days
    other_days_distance = (distance + first_day_distance) / 2

    # Calculate the total time John runs in a week
    total_time = first_day_distance + (other_days_distance * 2) / 2

    # Calculate John's speed in miles per week
    speed = total_distance / total_time

    # Display John's speed
    result = speed
    return result

print(solution())