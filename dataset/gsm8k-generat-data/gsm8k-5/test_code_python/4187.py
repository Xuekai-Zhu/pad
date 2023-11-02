def solution():
    computer_price = 3000  # Jeremy bought a computer for $3000
    accessories_price = computer_price * 0.1  # Accessories cost 10% of the price of the computer
    total_price = computer_price + accessories_price  # Total price of the purchase
    original_money = computer_price * 2  # Before the purchase, Jeremy had two times more money than the cost of the computer

    # Calculate how much money Jeremy has left after the purchase
    remaining_money = original_money - total_price
    result = remaining_money
    return result

print(solution())