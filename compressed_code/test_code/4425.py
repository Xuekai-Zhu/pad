def solution():
    
    current_balance = 126
    groceries = 60
    gas = groceries / 2
    towels_returned = 45
    new_balance = current_balance + groceries + gas - towels_returned
    result = new_balance
    return result

print(solution())