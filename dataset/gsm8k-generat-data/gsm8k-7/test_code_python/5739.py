def solution():
    dress_price = 80
    savings = 20
    weekly_allowance = 30
    arcade_spending = 10

    # Calculate total amount saved after n weeks of getting allowance
    weeks = 0
    total_saved = savings
    while total_saved < dress_price:
        weeks += 1
        total_saved += weekly_allowance - arcade_spending

    result = weeks
    return result

print(solution())