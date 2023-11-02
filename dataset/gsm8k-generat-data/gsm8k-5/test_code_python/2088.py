def solution():
    pasta_cost = 1.00  # cost of pasta per box
    sauce_cost = 2.00  # cost of sauce per jar
    meatball_cost = 5.00  # cost of meatballs per pound
    total_cost = pasta_cost + sauce_cost + (meatball_cost / 4)  # total cost of ingredients for 4 servings
    cost_per_serving = total_cost / 4  # cost per serving for 4 servings
    cost_per_serving_8 = cost_per_serving * 2  # cost per serving for 8 servings
    result = cost_per_serving_8
    return result

print(solution())