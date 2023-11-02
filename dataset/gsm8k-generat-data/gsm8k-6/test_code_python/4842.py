def solution():
    # Calculate the total cost of fruits before the discount
    lemons_cost = 6 * 2  # 6 lemons at $2 per lemon
    papayas_cost = 4 * 1  # 4 papayas at $1 per papaya
    mangos_cost = 2 * 4  # 2 mangos at $4 per mango
    total_cost = lemons_cost + papayas_cost + mangos_cost

    # Determine the number of $1 discounts Tom is eligible for
    total_fruits = 6 + 4 + 2  # 6 lemons, 4 papayas, 2 mangos
    num_discounts = total_fruits // 4

    # Apply the discounts and calculate the final cost
    final_cost = total_cost - num_discounts
    result = final_cost
    return result

print(solution())