def solution():
    shoes_cost = 74
    socks_cost = 2 * 2  # 2 pairs of socks that cost $2 per pair
    bag_cost = 42
    total_cost = shoes_cost + socks_cost + bag_cost

    if total_cost > 100:
        discount_amount = (total_cost - 100) * 0.1
        total_cost -= discount_amount

    result = total_cost
    return result

print(solution())