def solution():
    # Define the regular monthly cost and promotional cost
    regular_cost = 30
    promo_cost = regular_cost / 3

    # Calculate Mandy's total cost for the first 3 months
    first_3_months_cost = promo_cost * 3

    # Calculate Mandy's total cost for the first 4 months, including the extra fee
    first_4_months_cost = first_3_months_cost + regular_cost + 15

    # Calculate Mandy's total cost for the first 6 months, including the regular monthly cost
    total_cost = first_4_months_cost + 2 * regular_cost

    result = total_cost
    return result

print(solution())