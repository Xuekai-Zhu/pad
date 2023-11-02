def solution():
    hourly_wage = 10.0
    num_colleges = 6
    app_fee = 25.0

    # Calculate the total cost of all college applications
    total_cost = num_colleges * app_fee

    # Calculate the number of hours Linda needs to babysit to cover the application fees
    num_hours = total_cost / hourly_wage
    result = num_hours
    return result

print(solution())