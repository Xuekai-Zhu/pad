def solution():
    initial_balance = 126  # Marian's initial balance is $126.00
    grocery_charge = 60  # Marian puts $60.00 worth of groceries on her card
    gas_charge = grocery_charge / 2  # Marian puts half of the grocery amount in gas
    return_amount = 45  # Marian returns some bath towels for $45.00

    # Calculate the new balance on Marian's credit card
    new_balance = initial_balance + grocery_charge + gas_charge - return_amount
    result = new_balance
    return result

print(solution())