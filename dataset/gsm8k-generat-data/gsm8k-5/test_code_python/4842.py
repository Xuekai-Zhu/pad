def solution():
    # Calculate the total cost for lemons, papayas, and mangos separately
    lemons_cost = 6 * 2  # 6 lemons cost $2 each
    papayas_cost = 4 * 1  # 4 papayas cost $1 each
    mangos_cost = 2 * 4  # 2 mangos cost $4 each

    # Calculate the total number of fruits
    total_fruits = 6 + 4 + 2

    # Calculate the number of discounts Tom gets
    num_discounts = total_fruits // 4

    # Calculate the total discount and cost after discount
    total_discount = num_discounts * 1
    cost_after_discount = lemons_cost + papayas_cost + mangos_cost - total_discount

    result = cost_after_discount
    return result

print(solution())