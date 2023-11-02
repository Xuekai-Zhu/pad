def solution():
    num_nieces = 3
    mitts_cost = 14.0
    apron_cost = 16.0
    utensils_cost = 10.0
    knife_cost = utensils_cost * 2
    discount = 0.25  # 25% discount

    # Calculate the total cost of all cooking gear without discount
    total_cost = (mitts_cost + apron_cost + utensils_cost + knife_cost) * num_nieces

    # Calculate the discount amount
    discount_amount = total_cost * discount

    # Calculate the final cost after discount
    final_cost = total_cost - discount_amount
    result = final_cost
    return result

print(solution())