def solution():
    
    computer_price = 3000
    accessories_price = 0.1 * computer_price
    total_price = computer_price + accessories_price
    initial_money = 2 * computer_price
    remaining_money = initial_money - total_price
    result = remaining_money
    return result

print(solution())