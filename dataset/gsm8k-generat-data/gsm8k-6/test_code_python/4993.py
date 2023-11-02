def solution():
    # Calculate the total cost of buying one regular large pizza and three medium pizzas without the promotion
    regular_large_pizza_cost = 0 # price of regular large pizza is not given in the question
    medium_pizza_cost = 18
    total_cost_without_promotion = regular_large_pizza_cost + (3 * medium_pizza_cost)

    # Calculate the total cost of buying one regular large pizza and taking advantage of the promotion
    promotion_cost = regular_large_pizza_cost + (1 * medium_pizza_cost) + (3 * 5)  # $5 each for three medium pizzas
    total_savings = total_cost_without_promotion - promotion_cost
    result = total_savings
    return result

print(solution())