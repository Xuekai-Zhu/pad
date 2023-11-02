def solution():
    # Mike paid $5 for the DVD
    mike_cost = 5

    # Steve paid twice as much as Mike for the DVD
    steve_cost = 2 * mike_cost

    # Steve paid 80% of the cost of the DVD for shipping
    shipping_cost = 0.8 * steve_cost

    # Total cost for Steve is the DVD cost plus shipping cost
    total_cost = steve_cost + shipping_cost
    result = total_cost
    return result

print(solution())