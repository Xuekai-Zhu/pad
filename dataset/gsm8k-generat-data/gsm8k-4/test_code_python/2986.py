def solution():
    """Miley bought two cellphones for her parents. Each cellphone costs $800 but, since she is buying two units, she will receive a 5% discount for the total cost. How much did Miley pay?"""
    # Define the cost of each cellphone and the number of cellphones
    cellphone_cost = 800
    num_cellphones = 2

    # Calculate the total cost before discount
    total_cost_before_discount = cellphone_cost * num_cellphones

    # Calculate the amount of discount
    discount = total_cost_before_discount * 0.05

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount

    # Return the result
    result = total_cost_after_discount
    return result

print(solution())