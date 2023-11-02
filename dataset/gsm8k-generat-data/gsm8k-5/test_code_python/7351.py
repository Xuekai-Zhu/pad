def solution():
    cost = 120  # The cost of the elliptical machine is $120
    down_payment = cost / 2  # Rita makes a down payment equal to half the cost
    balance = cost - down_payment  # Rita still owes the balance

    # Calculate the daily minimum amount Rita must pay
    minimum_daily_payment = balance / 10  # Rita has to pay the balance within 10 days

    result = minimum_daily_payment
    return result

print(solution())