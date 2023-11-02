def solution():
    apple_price = 14/12  # price per apple
    kiwi_cost = 10
    banana_cost = kiwi_cost / 2
    total_spent = kiwi_cost + banana_cost

    total_funds = 50  # total amount of money Brian has
    subway_fare = 2 * 3.5  # round trip subway fare

    remaining_funds = total_funds - total_spent - subway_fare

    max_apples = remaining_funds // apple_price

    result = max_apples
    return result

print(solution())