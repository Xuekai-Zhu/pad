def solution():
    peaches_price = 2.0
    plums_price = 1.0
    apricots_price = 3.0
    peaches_weight = 6
    plums_weight = 8
    apricots_weight = 6

    # Calculate the total cost of peaches
    peaches_cost = peaches_price * peaches_weight

    # Calculate the total cost of plums
    plums_cost = plums_price * plums_weight

    # Calculate the total cost of apricots
    apricots_cost = apricots_price * apricots_weight

    # Calculate the total cost of all fruit
    total_cost = peaches_cost + plums_cost + apricots_cost
    result = total_cost
    return result

print(solution())