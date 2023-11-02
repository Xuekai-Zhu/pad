def solution():
    hours_per_week = 20
    num_months = 2
    num_weeks = num_months * 4

    # Calculate the total number of hours Chris was supposed to work
    total_hours_chris = hours_per_week * num_weeks

    # Subtract the one week Chris was sick and Cathy filled in for her
    total_hours_chris -= hours_per_week

    # Calculate the total number of hours Cathy worked
    total_hours_cathy = hours_per_week * num_weeks

    result = total_hours_cathy
    return result

print(solution())