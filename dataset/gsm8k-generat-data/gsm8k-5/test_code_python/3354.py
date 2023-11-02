def solution():
    inheritance = 20000  # Mr. Lalande inherited 20,000 euros
    car_price = 18000  # The car Mr. Lalande wants to buy costs 18000 euros
    initial_payment = 3000  # Mr. Lalande pays 3000 euros initially

    # Calculate the remaining amount Mr. Lalande has to pay
    remaining_amount = car_price - initial_payment
    # Calculate the monthly installment
    monthly_installment = remaining_amount / 6
    result = monthly_installment
    return result

print(solution())