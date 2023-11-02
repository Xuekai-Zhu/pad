def solution():
    """Barbara wants to save up for a new wristwatch that costs $100. Her parents give her an allowance of $5 a week and she can either save it all up for the watch or spend it as she wishes. 10 weeks pass and due to spending some of her money on ice cream, Barbara currently only has $20. How many more weeks does she need to save for a watch if she stops spending on other things right now?"""
    watch_cost = 100
    current_savings = 20
    weekly_allowance = 5
    weeks_to_save = (watch_cost - current_savings) / weekly_allowance
    result = weeks_to_save
    return result

print(solution())