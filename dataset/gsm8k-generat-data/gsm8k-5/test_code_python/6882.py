def solution():
    pay = 5000  # Brendan earned $5000 in June
    car_cost = 1500  # Brendan bought a used car for $1500
    recharge_amount = pay / 2  # Brendan recharges his debit card with half of his pay

    # Calculate the total amount of remaining money after buying the car
    remaining_money = pay - car_cost - recharge_amount
    result = remaining_money
    return result

print(solution())