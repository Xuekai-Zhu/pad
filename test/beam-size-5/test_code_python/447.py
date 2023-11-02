def solution():
    initial_cost = 900  # The initial cost of filling up 20 helium balloons
    increased_cost = 20  # The cost of filling each balloon was increased by $20
    additional_cost = 20  # The additional cost of filling each balloon was increased by $20
    num_balloons = 170  # Bentley wants to fill 170 balloons

    # Calculate the total cost of filling the balloons after the price increase
    total_cost_after_price_increase = initial_cost + (additional_cost * num_balloons)

    # Calculate the total cost of filling the balloons after the price increase
    total_cost_after_price_increase = total_cost_after_price_increase + additional_cost
    result = total_cost_after_price_increase
    return result

print(solution())