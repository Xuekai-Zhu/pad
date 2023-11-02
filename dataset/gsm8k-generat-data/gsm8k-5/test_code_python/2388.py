def solution():
    apples_cost_per_dozen = 40  # Apples cost 40 dollars per dozen
    pears_cost_per_dozen = 50  # Pears cost 50 dollars per dozen
    num_dozen_of_each = 14  # Hank bought 14 dozen of each kind of fruit

    # Calculate the total cost of apples and pears
    total_apple_cost = apples_cost_per_dozen * num_dozen_of_each
    total_pear_cost = pears_cost_per_dozen * num_dozen_of_each
    total_cost = total_apple_cost + total_pear_cost
    result = total_cost
    return result

print(solution())