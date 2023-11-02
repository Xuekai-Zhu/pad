def solution():
    """Marian's pending credit card balance is $126.00. She puts $60.00 worth of groceries on her card and half that amount in gas. She returned some bath towels for $45.00. What's the new balance on her credit card?"""
    current_balance = 126
    groceries = 60
    gas = groceries / 2
    towels_returned = 45
    new_balance = current_balance + groceries + gas - towels_returned
    result = new_balance
    return result

print(solution())