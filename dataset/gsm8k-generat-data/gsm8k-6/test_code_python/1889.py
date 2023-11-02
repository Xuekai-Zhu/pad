def solution():
    # Find how much Reed and Quinn spend on their toys
    reed_spending = 80 - 20  # Trevor always spends $20 more than Reed
    quinn_spending = reed_spending / 2  # Reed spends 2 times as much money as Quinn

    # Calculate the total spending of the three friends in one year
    total_spending = 80 + reed_spending + quinn_spending

    # Calculate the total spending of the three friends in four years
    total_spending_4_years = total_spending * 4
    result = total_spending_4_years
    return result

print(solution())