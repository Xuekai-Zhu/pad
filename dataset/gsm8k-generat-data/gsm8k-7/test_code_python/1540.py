def solution():
    principal = 10000
    rate = 0.20
    time = 3

    # Calculate the amount of money Sam has after compounding interest for 3 years
    amount = principal * ((1 + rate) ** time)

    # Calculate the amount of additional money Sam needs to invest to have three times as much invested
    additional_investment = amount * 2

    # Calculate the total amount of money Sam has after investing the additional amount and getting a 15% return
    total_amount = amount + (additional_investment * 1.15)

    result = total_amount
    return result

print(solution())