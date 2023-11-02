def solution():
    # Calculate the total cost of the cellphones before the discount
    total_cost = 2 * 800  # each cellphone costs $800 and she buys two units

    # Calculate the amount of discount she will receive
    discount = 0.05 * total_cost

    # Calculate the final cost after the discount
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())