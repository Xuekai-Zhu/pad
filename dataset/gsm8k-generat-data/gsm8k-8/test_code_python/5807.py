def solution():
    # Calculate the time spent on Saturday
    saturday_rounds = 1 + 10
    saturday_time = saturday_rounds * 30

    # Calculate the time spent on Sunday
    sunday_time = 15 * 30

    # Calculate the total time spent
    total_time = saturday_time + sunday_time
    result = total_time
    return result

print(solution())