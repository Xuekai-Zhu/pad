def solution():
    """Mark gets a new phone plan that is 30% more expensive than his old plan. If his old plan was $150 a month how much does his new plan cost?"""
    # Define the old plan cost and the percentage increase
    old_plan_cost = 150
    percentage_increase = 30

    # Calculate the new plan cost
    new_plan_cost = old_plan_cost * (1 + percentage_increase/100)

    # return the result
    result = new_plan_cost
    return result

print(solution())