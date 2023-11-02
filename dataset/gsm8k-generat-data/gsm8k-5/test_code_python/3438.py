def solution():
    # Initialize variables
    money_made = 0
    daily_income = 10

    # Calculate money made after 5 days
    for i in range(5):
        money_made += daily_income
        daily_income += 4

    result = money_made
    return result

print(solution())