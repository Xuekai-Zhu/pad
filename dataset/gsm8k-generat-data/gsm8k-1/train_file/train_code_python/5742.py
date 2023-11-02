def solution():
    """Mark gets a new phone plan that is 30% more expensive than his old plan. If his old plan was $150 a month how much does his new plan cost?"""
    old_plan_cost = 150
    percent_increase = 30
    increase_amount = old_plan_cost * (percent_increase / 100)
    new_plan_cost = old_plan_cost + increase_amount
    result = new_plan_cost
    return result

print(solution())