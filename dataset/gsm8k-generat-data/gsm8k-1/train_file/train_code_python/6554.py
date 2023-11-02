def solution():
    """James injured his ankle and decides to slowly start working back up to his previous running goals and then surpass them. Before the injury, he was able to run 100 miles per week. He wants to get up to 20% more than that total in 280 days and each week he will increase miles walked in the week by the same amount. How many miles does he need to add per week?"""
    initial_miles_per_week = 100
    target_percent_increase = 20
    target_total_miles = initial_miles_per_week * (1 + (target_percent_increase/100))
    weeks_to_reach_target = 280/7  # 280 days = 40 weeks
    additional_miles_per_week = (target_total_miles - initial_miles_per_week) / weeks_to_reach_target
    result = additional_miles_per_week
    return result

print(solution())