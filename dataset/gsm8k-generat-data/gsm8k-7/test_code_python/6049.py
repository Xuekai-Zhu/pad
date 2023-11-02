def solution():
    cherries_price = 5
    olives_price = 7
    num_bags = 50
    discount = 0.1  # 10% discount

    # Calculate the total cost of 50 bags of cherries
    total_cherries_cost = cherries_price * num_bags

    # Calculate the total cost of 50 bags of olives
    total_olives_cost = olives_price * num_bags

    # Calculate the total cost of all items before discount
    total_cost_before_discount = total_cherries_cost + total_olives_cost

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount * (1 - discount)

    result = total_cost_after_discount
    return result

print(solution())