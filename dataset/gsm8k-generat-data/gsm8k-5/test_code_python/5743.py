def solution():
    old_plan_cost = 150  # Mark's old plan cost $150 a month
    percent_increase = 30  # Mark's new plan is 30% more expensive than his old plan
    
    # Calculate the new plan cost
    new_plan_cost = old_plan_cost * (1 + percent_increase/100)
    result = new_plan_cost
    return result

print(solution())