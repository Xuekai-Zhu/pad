def solution():
    initial_money = 450
    computer_price = 400
    printer_price = 40

    # Calculate the total amount spent on the computer and printer
    total_spent = computer_price + printer_price

    # Calculate the amount of money left
    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())