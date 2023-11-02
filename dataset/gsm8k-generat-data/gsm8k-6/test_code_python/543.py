def solution():
    # Calculate the total amount collected by the class
    full_payers = 25 - 4  # number of students who paid the full amount
    total_amount = (full_payers * 50) + (4 * 25)  # full payers paid $50, half payers paid $25
    result = total_amount
    return result

print(solution())