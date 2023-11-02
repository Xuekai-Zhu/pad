def solution():
    initial_weight = 60
    percent_increase = 60
    increase_amount = initial_weight * (percent_increase / 100)
    new_weight = initial_weight + increase_amount
    num_ingots = new_weight / 2
    if num_ingots <= 10:
        cost = num_ingots * 5
    else:
        cost = (num_ingots * 5) * 0.8
    result = cost
    return result

print(solution())