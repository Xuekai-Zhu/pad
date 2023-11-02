def solution():
    """Miley bought two cellphones for her parents. Each cellphone costs $800 but, since she is buying two units, she will receive a 5% discount for the total cost. How much did Miley pay?"""
    # Define the cost of each cellphone
    CELLPHONE_COST = 800

    # Define the number of cellphones Miley is buying
    num_cellphones = 2

    # Calculate the total cost before the discount
    total_cost_before_discount = CELLPHONE_COST * num_cellphones

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * 0.05

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    # Display the total cost that Miley paid
    result = total_cost_after_discount
    return result

print(solution())