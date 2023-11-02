def solution():
    previous_weekly_mileage = 100  # James was able to run 100 miles per week before the injury
    target_total_mileage = 100 * 1.2  # James wants to run 20% more than his previous total mileage
    weeks_to_reach_target = 280 / 7  # James has 280 days to reach his target, or 40 weeks

    # Calculate the total amount of mileage James needs to add over the 40 weeks
    total_additional_mileage = target_total_mileage - (previous_weekly_mileage * weeks_to_reach_target)

    # Calculate the additional mileage James needs to add each week to reach his target
    additional_mileage_per_week = total_additional_mileage / weeks_to_reach_target
    result = additional_mileage_per_week
    return result

print(solution())