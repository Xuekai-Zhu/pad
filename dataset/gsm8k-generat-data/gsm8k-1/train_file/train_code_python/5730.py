def solution():
    """Marian's pending credit card balance is $126.00. She puts $60.00 worth of groceries on her card and half that amount in gas.
    She returned some bath towels for $45.00. What's the new balance on her credit card?"""
    initial_balance = 126
    grocery_cost = 60
    gas_cost = grocery_cost / 2
    return_amount = 45

    new_balance = initial_balance + grocery_cost + gas_cost - return_amount

    return new_balance

print(solution())