def solution():
    
    computer_price = 3000
    accessory_price = computer_price * 0.1
    total_price = computer_price + accessory_price
    initial_money = computer_price * 2
    final_money = initial_money - total_price
    result = final_money
    return result

print(solution())