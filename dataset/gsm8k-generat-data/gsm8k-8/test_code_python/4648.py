def solution():
    # Define the earnings and expenses
    earnings = 18 * 80
    expenses = 280

    # Calculate the amount allocated for recreation and relaxation
    rec_allocation = 0.2 * earnings

    # Calculate the amount saved
    amount_saved = earnings - expenses - rec_allocation
    
    result = amount_saved
    return result

print(solution())