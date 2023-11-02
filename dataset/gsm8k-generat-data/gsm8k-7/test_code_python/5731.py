def solution():
    pending_balance = 126.00
    groceries = 60.00
    gas = groceries / 2
    returned_towels = 45.00

    # Calculate the total amount charged to her card
    total_charged = groceries + gas

    # Calculate the new balance on her credit card
    new_balance = pending_balance + total_charged - returned_towels
    result = new_balance
    return result

print(solution())