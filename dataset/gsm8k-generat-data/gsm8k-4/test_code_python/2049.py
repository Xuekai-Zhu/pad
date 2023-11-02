def solution():
    """Mark and his sister Chris both leave their house for school at the same time.  Mark travels at the same speed as Chris, who walks 3 miles per hour. After walking 3 miles Mark has to turn around and go home because he forgot his lunch. If the distance from their house to the school is 9 miles, how much longer does Mark spend walking than Chris?"""
    # Define the distance from their house to the school and Chris's walking speed
    distance = 9
    chris_speed = 3

    # Calculate the time it takes for Chris to walk to school
    chris_time = distance / chris_speed

    # Calculate the distance Mark walks before turning back
    mark_distance = 3

    # Calculate the remaining distance for Mark to walk to school after turning back
    remaining_distance = distance - mark_distance

    # Calculate the time it takes for Mark to walk to his house and back to where he turned around
    mark_time = (mark_distance * 2) / chris_speed

    # Calculate the total time it takes for Mark to walk to school
    total_mark_time = mark_time + (remaining_distance / chris_speed)

    # Calculate the difference in time between Mark and Chris
    time_difference = total_mark_time - chris_time

    # Return the result in minutes
    result = time_difference * 60
    return result

print(solution())