def solution():
    bodyguard_rate = 20
    hours_per_day = 8
    days_per_week = 7
    num_bodyguards = 2

    # Calculate the total number of hours worked by both bodyguards in one week
    total_hours = hours_per_day * days_per_week * num_bodyguards

    # Calculate the total cost of hiring the bodyguards for one week
    total_cost = total_hours * bodyguard_rate
    result = total_cost
    return result

print(solution())