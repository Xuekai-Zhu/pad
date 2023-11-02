def solution():
    # Define variables
    starting_miles = 100
    target_days = 280
    target_percentage_increase = 0.2

    # Calculate target miles
    target_miles = starting_miles * (1 + target_percentage_increase)

    # Calculate days per week
    days_per_week = 7

    # Calculate weeks to reach target
    weeks_to_reach_target = target_days / days_per_week

    # Calculate miles per week to reach target
    miles_per_week = (target_miles - starting_miles) / weeks_to_reach_target

    result = miles_per_week
    return result

print(solution())