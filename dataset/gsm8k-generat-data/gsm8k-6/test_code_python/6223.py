def solution():
    # Calculate the cost of buying 2 chocolates per week for 3 weeks in the local store
    local_store_cost = 2 * 3 * 3  # 2 chocolates per week, each costing $3, for 3 weeks

    # Calculate the cost of buying 2 chocolates per week for 3 weeks in the promotion store
    promotion_store_cost = 2 * 2 * 3  # 2 chocolates per week, each costing $2, for 3 weeks

    # Calculate the amount saved by buying in the promotion store
    amount_saved = local_store_cost - promotion_store_cost
    result = amount_saved
    return result

print(solution())