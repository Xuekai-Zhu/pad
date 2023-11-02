def solution():
    # Calculate the cost of James' weight vest
    vest_cost = 250

    # Calculate the cost of the weight plates
    weight_plate_cost = 1.2 * 200

    # Calculate the cost of a 200-pound weight vest with discount
    discount_cost = 700 - 100

    # Calculate the amount James saves with his vest
    savings = discount_cost - (vest_cost + weight_plate_cost)

    result = savings
    return result

print(solution())