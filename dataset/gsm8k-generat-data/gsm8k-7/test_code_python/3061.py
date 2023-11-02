def solution():
    hourly_rate = 10
    first_month_hours = 35
    second_month_hours = first_month_hours + 5

    # Calculate the total hours tutored
    total_hours = first_month_hours + second_month_hours

    # Calculate the total earnings
    total_earnings = total_hours * hourly_rate

    # Calculate the amount spent on personal needs
    personal_spending = 4/5 * total_earnings

    # Calculate the amount saved
    amount_saved = total_earnings - personal_spending
    result = amount_saved
    return result

print(solution())