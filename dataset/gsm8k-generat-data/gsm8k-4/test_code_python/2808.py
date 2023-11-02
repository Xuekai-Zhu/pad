def solution():
    """Rob and Mark plan to meet at the national park. It takes 1 hour for Rob to get to the national park and it takes three times as much time for Mark to get to the national park. If Rob leaves his home at 11 a.m., at what time should Mark leave his home so that they both arrive at the same time?"""
    # Define the time it takes for Rob to get to the national park
    rob_time = 1

    # Calculate the time it takes for Mark to get to the national park
    mark_time = rob_time * 3

    # Calculate the time Mark should leave his home
    mark_leave_time = "2:00 PM" # calculated manually by adding rob_time and mark_time to 11 a.m.

    # return the result
    result = mark_leave_time
    return result

print(solution())