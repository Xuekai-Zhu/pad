def solution():
    # Calculate the total cost of shorts and shoes
    shorts_cost = 5 * 7  # 5 pairs of shorts for $7 each
    shoes_cost = 2 * 10  # 2 pairs of shoes for $10 each
    total_cost = 75 - shorts_cost - shoes_cost  # total cost minus cost of shorts and shoes

    # Calculate the cost of each top
    cost_per_top = total_cost / 4  # divide remaining cost by 4 tops
    result = cost_per_top
    return result

print(solution())