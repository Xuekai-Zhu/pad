def solution():
    """Julia has a parrot and a rabbit. She buys food for both of the animals for $30 in total a week. Julia has the rabbit for 5 weeks, and the parrot for 3 weeks. How much money did Julia already spend on food for her animals, if the weekly cost of the rabbit food is $12?"""
    rabbit_weekly_cost = 12
    total_weeks = 5 + 3
    total_cost = 30 * total_weeks
    parrot_weekly_cost = (total_cost - (rabbit_weekly_cost*5)) / 3
    total_spent = (rabbit_weekly_cost * 5) + (parrot_weekly_cost * 3)
    result = total_spent
    return result

print(solution())