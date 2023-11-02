def solution():
    """Jeremy bought a computer for $3000, and some accessories for 10% of the price of the computer. How much money has Jeremy if, before the purchase, he had two times more money, than the cost of the computer itself?"""
    computer_price = 3000
    accessory_price = computer_price * 0.1
    total_price = computer_price + accessory_price
    initial_money = computer_price * 2
    final_money = initial_money - total_price
    result = final_money
    return result

print(solution())