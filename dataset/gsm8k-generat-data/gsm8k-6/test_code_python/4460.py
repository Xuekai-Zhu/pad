def solution():
    # Calculate the cost of James' weight vest and weight plates
    vest_cost = 250
    weight_plate_cost = 200 * 1.2
    total_cost = vest_cost + weight_plate_cost

    # Calculate the cost of a 200-pound weight vest with discount
    discounted_cost = 700 - 100

    # Calculate the amount saved by James
    amount_saved = discounted_cost - total_cost
    result = amount_saved
    return result

print(solution())