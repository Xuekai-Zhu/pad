def solution():
    """Mark gets a new phone plan that is 30% more expensive than his old plan. If his old plan was $150 a month how much does his new plan cost?"""
    old_plan_price = 150
    increase_percent = 30
    new_plan_price = old_plan_price + (old_plan_price * increase_percent / 100)
    result = new_plan_price
    return result

print(solution())