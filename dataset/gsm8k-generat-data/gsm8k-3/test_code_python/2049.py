def solution():
    """Mark and his sister Chris both leave their house for school at the same time.  Mark travels at the same speed as Chris, who walks 3 miles per hour. After walking 3 miles Mark has to turn around and go home because he forgot his lunch. If the distance from their house to the school is 9 miles, how much longer does Mark spend walking than Chris?"""
    # Calculate the time it takes Chris to walk to school
    chris_time = 9 / 3

    # Calculate the time it takes Mark to walk to the point where he turns around
    mark_turnaround_time = 3 / 3

    # Calculate the time it takes Mark to walk back home
    mark_return_time = 3 / (3*2)

    # Calculate the total time Mark spends walking
    mark_total_time = mark_turnaround_time + mark_return_time

    # Calculate the difference in time spent walking between Mark and Chris
    time_difference = mark_total_time - chris_time

    # Display the time difference
    result = time_difference
    return result

print(solution())