def solution():
    requests_per_day = 6  # Maia gets 6 client requests every day
    requests_per_workday = 4  # Maia works on 4 requests each day
    workdays = 5  # Maia works for 5 days

    # Calculate the total number of client requests Maia will work on in 5 days
    total_requests_worked_on = requests_per_workday * workdays

    # Calculate the total number of client requests remaining to work on after 5 days
    requests_remaining = (requests_per_day * workdays) - total_requests_worked_on
    result = requests_remaining
    return result

print(solution())