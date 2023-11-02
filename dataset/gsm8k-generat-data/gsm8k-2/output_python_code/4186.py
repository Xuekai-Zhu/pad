def solution():
    """Jeremy bought a computer for $3000, and some accessories for 10% of the price of the computer. How much money has Jeremy if,
    before the purchase, he had two times more money, than the cost of the computer itself?"""
    computer_price = 3000
    accessories_price = 0.1 * computer_price
    total_price = computer_price + accessories_price
    initial_money = 2 * computer_price
    remaining_money = initial_money - total_price
    result = remaining_money
    return result

print(solution())