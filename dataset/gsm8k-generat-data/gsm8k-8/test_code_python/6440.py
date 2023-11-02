def solution():
    # Calculate the cost of one uniform without discount
    uniform_cost_no_discount = 7.5 + 15 + 4.5

    # Calculate the cost of one uniform with discount
    uniform_cost_with_discount = 6.75 + 13.5 + 3.75

    # Calculate the total cost of uniforms without discount
    total_cost_no_discount = uniform_cost_no_discount * 12

    #Calculate the total cost of uniforms with discount
    total_cost_with_discount = uniform_cost_with_discount * 12

    # Calculate the amount saved with the discount
    amount_saved = total_cost_no_discount - total_cost_with_discount
    result = amount_saved
    return result

print(solution())