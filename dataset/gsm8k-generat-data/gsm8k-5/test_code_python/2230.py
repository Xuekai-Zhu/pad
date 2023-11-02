def solution():
    wage_per_day = 6  # Alfonso earns $6 per day
    helmet_cost = 340  # The cost of the mountain bike helmet is $340
    current_savings = 40  # Alfonso currently has $40 saved up
    days_per_week = 5  # Alfonso walks his aunt's dog 5 days per week

    # Calculate the total amount Alfonso needs to save
    total_savings_needed = helmet_cost - current_savings

    # Calculate how many days it will take to save up enough money
    days_needed = total_savings_needed / wage_per_day / days_per_week

    # Round up to the nearest week
    weeks_needed = math.ceil(days_needed / 7)

    result = weeks_needed
    return result

print(solution())