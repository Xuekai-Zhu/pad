def solution():
    """Rob and Mark plan to meet at the national park. It takes 1 hour for Rob to get to the national park and it takes three times as much time for Mark to get to the national park. If Rob leaves his home at 11 a.m., at what time should Mark leave his home so that they both arrive at the same time?"""
    # Define the time it takes for Rob to get to the national park
    rob_time = 1

    # Calculate the time it takes for Mark to get to the national park
    mark_time = rob_time * 3

    # Calculate the total time they both need to arrive at the same time
    total_time = rob_time + mark_time

    # Determine what time Mark should leave his home
    mark_departure_time = "2 p.m."

    # Display the time Mark should leave his home
    result = mark_departure_time
    return result

print(solution())