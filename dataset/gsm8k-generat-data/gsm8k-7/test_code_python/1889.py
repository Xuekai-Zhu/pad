def solution():
    trevor_spending = 80
    reed_spending = trevor_spending - 20
    quinn_spending = reed_spending / 2

    # Calculate the total spending of the three friends in one year
    total_spending = trevor_spending + reed_spending + quinn_spending

    # Calculate the total spending of the three friends in four years
    total_spending_four_years = total_spending * 4
    result = total_spending_four_years
    return result

print(solution())