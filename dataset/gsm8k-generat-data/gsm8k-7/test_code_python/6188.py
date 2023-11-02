def solution():
    hours_10 = 20
    pay_10 = 10
    hours_20 = 30
    pay_20 = 20
    hours_40 = 5
    pay_40 = 40
    expenses = 500

    # Calculate the total earnings from working 20 hours at $10/hr
    earnings_10 = hours_10 * pay_10

    # Calculate the total earnings from working 30 hours at $20/hr
    earnings_20 = hours_20 * pay_20

    # Calculate the total earnings from working 5 hours at $40/hr
    earnings_40 = hours_40 * pay_40

    # Calculate the total earnings from all gigs
    total_earnings = earnings_10 + earnings_20 + earnings_40

    # Calculate the remaining balance after expenses
    balance = total_earnings - expenses
    result = balance
    return result

print(solution())