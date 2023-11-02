def solution():
    car_price = 13380  # Mr. Dubois buys a new car for $13,380
    initial_payment = 5400  # Mr. Dubois pays $5,400 initially
    monthly_payment = 420  # Mr. Dubois pays $420 per month after the initial payment
    remaining_balance = car_price - initial_payment  # Mr. Dubois still owes this much after the initial payment

    # Calculate the number of months required to pay off the remaining balance
    months = remaining_balance / monthly_payment
    result = months
    return result

print(solution())