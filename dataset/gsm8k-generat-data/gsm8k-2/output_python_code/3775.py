def solution():
    """Julia has a parrot and a rabbit. She buys food for both of the animals for $30 in total a week. Julia has the rabbit for 5 weeks, and the parrot for 3 weeks. How much money did Julia already spend on food for her animals, if the weekly cost of the rabbit food is $12?"""
    rabbit_weekly_cost = 12
    parrot_weekly_cost = 30 - rabbit_weekly_cost
    rabbit_duration = 5
    parrot_duration = 3
    rabbit_total_cost = rabbit_weekly_cost * rabbit_duration
    parrot_total_cost = parrot_weekly_cost * parrot_duration
    total_cost = rabbit_total_cost + parrot_total_cost
    result = total_cost
    return result

print(solution())