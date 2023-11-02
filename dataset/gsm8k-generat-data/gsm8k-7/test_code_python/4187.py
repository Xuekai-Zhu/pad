def solution():
    computer_price = 3000

    # Calculate the amount spent on accessories
    accessories_price = computer_price * 0.1

    # Calculate the total amount spent
    total_price = computer_price + accessories_price

    # Calculate the amount of money Jeremy had before the purchase
    initial_money = computer_price * 2

    # Calculate the money left after the purchase
    money_left = initial_money - total_price
    result = money_left
    return result

print(solution())