def solution():
    total_debt = 100
    amount_paid = 40
    remaining_debt = total_debt - amount_paid
    hourly_rate = 15

    # Calculate the number of hours Jake needs to work to pay off his debt
    hours_worked = remaining_debt / hourly_rate
    result = hours_worked
    return result

print(solution())