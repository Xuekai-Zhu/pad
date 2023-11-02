def solution():
    total_bowls = 70  # Howard has a collection of 70 wooden bowls
    customers = 20  # There were 20 customers that day
    bought_20 = customers // 2  # Half of the customers bought 20 bowls each
    bought_10 = customers - bought_20  # The rest of the customers bought 10 bowls each

    # Calculate the number of bowls awarded as rewards
    rewards = (bought_10 // 10) * 2 + (bought_20 // 10) * 2

    # Calculate the number of bowls remaining in the collection
    remaining_bowls = total_bowls - rewards
    result = remaining_bowls
    return result

print(solution())