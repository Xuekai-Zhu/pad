def solution():
    lunch_time = 30  # Bobby takes a 30 min lunch
    break_time = 2  # Bobby takes 2 15 minutes break per day
    num_days = 5  # Bobby wants to know how many hours his lunches and breaks add up to

    # Calculate the total time Bobby spends lunches in 5 days
    total_lunch_time = lunch_time * num_days

    # Calculate the total time Bobby spends breakes in 5 days
    total_break_time = break_time * num_days

    # Calculate the total time Bobby spends lunches and breaks in 5 days
    total_time = total_lunch_time + total_break_time

    # Convert the total time to hours
    hours = total_time / 60
    result = hours
    return result

print(solution())