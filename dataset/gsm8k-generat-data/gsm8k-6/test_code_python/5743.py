def solution():
    # Calculate the cost of Mark's new phone plan
    old_plan = 150  # cost of Mark's old plan
    increase_percent = 30  # percent increase of the new plan
    increase_amount = (increase_percent/100) * old_plan  # amount of increase in cost
    new_plan = old_plan + increase_amount  # cost of Mark's new plan
    result = new_plan
    return result

print(solution())