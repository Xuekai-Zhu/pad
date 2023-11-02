def solution():
    # Define Brendan's earnings and expenses
    earnings = 5000
    car_cost = 1500

    # Calculate the amount Brendan recharged his debit card with
    recharge_amount = earnings / 2

    # Calculate Brendan's remaining money after buying the car
    remaining_money = earnings - car_cost - recharge_amount
    result = remaining_money
    return result

print(solution())