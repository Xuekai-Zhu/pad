def solution():
    num_family_members = 5
    cost_soda = 0.5  # Each bottle of soda costs $0.5
    cost_pizza = 1  # Each slice of pizza costs $1
    num_sodas = num_family_members + 1  # Zoe needs one soda for herself and one for each family member
    num_slices_pizza = 2 * num_family_members  # Zoe buys 2 slices of pizza per family member

    # Calculate the total cost of Zoe's purchases
    total_cost = num_sodas * cost_soda + num_slices_pizza * cost_pizza

    result = total_cost
    return result

print(solution())