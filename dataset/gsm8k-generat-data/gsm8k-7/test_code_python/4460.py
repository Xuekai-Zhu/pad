def solution():
    weight_vest_cost = 250
    weight_plate_cost = 1.2
    discount = 100

    # Calculate the total cost of the weight plates
    total_weight_plate_cost = 200 * weight_plate_cost

    # Calculate the cost of the 200-pound weight vest after discount
    weight_vest_cost_after_discount = 700 - discount

    # Calculate the total cost of James' purchase
    total_cost = weight_vest_cost + total_weight_plate_cost

    # Calculate the cost if James bought the 200-pound weight vest
    cost_of_200_pound_vest = weight_vest_cost_after_discount

    # Calculate the amount James saved
    amount_saved = cost_of_200_pound_vest - total_cost

    result = amount_saved
    return result

print(solution())