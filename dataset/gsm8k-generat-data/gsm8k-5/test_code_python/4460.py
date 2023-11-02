def solution():
    # Calculate the cost of the weight plates
    weight_plate_cost = 200 * 1.2

    # Calculate the cost of the 200-pound weight vest with discount
    weight_vest_cost = 600  # 200-pound weight vest costs $700, but there's a $100 discount
    weight_vest_cost_with_discount = weight_vest_cost - 100

    # Calculate the total cost of James' purchase
    total_cost = 250 + weight_plate_cost

    # Calculate how much James saved with his weight vest
    saved_amount = weight_vest_cost_with_discount - total_cost
    result = saved_amount
    return result

print(solution())