def solution():
    earnings = 200
    lunch_spending = earnings / 4
    dvd_spending = earnings / 2

    # Calculate the total amount spent
    total_spending = lunch_spending + dvd_spending

    # Calculate the amount left
    amount_left = earnings - total_spending
    result = amount_left
    return result

print(solution())