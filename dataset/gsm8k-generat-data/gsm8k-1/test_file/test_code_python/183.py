def solution():
    """Mandy owes Benedict $100. They agreed to have monthly interest of 2%. If Mandy was able to pay it after 3 months, how much should she give to Benedict?"""
    amount_owed = 100
    interest_rate = 0.02
    months = 3
    interest = amount_owed * interest_rate * months
    total_amount = amount_owed + interest
    result = total_amount
    return result

print(solution())