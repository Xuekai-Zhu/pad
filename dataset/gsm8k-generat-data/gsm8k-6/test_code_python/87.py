def solution():
    initial_weight = 400  # in pounds
    final_weight = 1.5 * initial_weight  # in pounds
    increase = final_weight - initial_weight  # in pounds
    value_increase = increase * 3  # value increase in dollars
    result = value_increase
    return result

print(solution())