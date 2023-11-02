def solution():
    """Jeremy bought a computer for $3000, and some accessories for 10% of the price of the computer. How much money has Jeremy if, before the purchase, he had two times more money, than the cost of the computer itself?"""
    # Define the initial amount of money Jeremy had
    initial_money = 6000

    # Define the price of the computer and the accessories
    computer_price = 3000
    accessories_price = computer_price * 0.1

    # Calculate the total cost of the purchase
    total_cost = computer_price + accessories_price

    # Calculate how much money Jeremy has left after the purchase
    remaining_money = initial_money - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())