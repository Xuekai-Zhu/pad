def solution():
    """Marian's pending credit card balance is $126.00. She puts $60.00 worth of groceries on her card and half that amount in gas. She returned some bath towels for $45.00. What's the new balance on her credit card?"""
    # Define the initial credit card balance
    initial_balance = 126.00

    # Add the cost of groceries and gas to the balance
    groceries_cost = 60.00
    gas_cost = groceries_cost / 2
    new_balance = initial_balance + groceries_cost + gas_cost

    # Subtract the amount refunded for the bath towels
    bath_towel_refund = 45.00
    new_balance -= bath_towel_refund

    # Return the new balance
    result = new_balance
    return result

print(solution())