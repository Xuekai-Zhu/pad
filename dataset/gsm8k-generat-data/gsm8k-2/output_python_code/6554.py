def solution():
    """James injured his ankle and decides to slowly start working back up to his previous running goals and then surpass them. Before the injury, he was able to run 100 miles per week. He wants to get up to 20% more than that total in 280 days and each week he will increase miles walked in the week by the same amount. How many miles does he need to add per week?"""
    starting_miles = 100
    goal_percent_increase = 0.2
    goal_miles = starting_miles * (1 + goal_percent_increase)
    num_weeks = 40
    extra_miles_per_week = (goal_miles - starting_miles) / num_weeks
    result = extra_miles_per_week
    return result

print(solution())