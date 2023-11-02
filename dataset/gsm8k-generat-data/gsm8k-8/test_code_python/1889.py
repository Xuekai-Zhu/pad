def solution():
    # Calculate how much money Reed spends on toys
    reed_spending = 80 - 20
    # Calculate how much money Quinn spends on toys
    quinn_spending = reed_spending / 2

    # Calculate total spending per year for all three friends
    total_spending = 80 + reed_spending + quinn_spending

    # Calculate total spending for 4 years
    total_spending_4_years = total_spending * 4
    result = total_spending_4_years
    return result

print(solution())