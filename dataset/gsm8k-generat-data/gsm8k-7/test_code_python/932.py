def solution():
    num_daily_client_requests = 6
    num_daily_worked_on = 4
    num_days = 5

    # Calculate the total number of client requests Maia will receive
    total_client_requests = num_daily_client_requests * num_days

    # Calculate the total number of client requests Maia will work on
    total_worked_on = num_daily_worked_on * num_days

    # Calculate the number of client requests remaining to work on after 5 days
    remaining_requests = total_client_requests - total_worked_on
    result = remaining_requests
    return result

print(solution())