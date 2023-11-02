def solution():
    """Jeremy bought a computer for $3000, and some accessories for 10% of the price of the computer. How much money has Jeremy if, before the purchase, he had two times more money, than the cost of the computer itself?"""
    # Calculate the cost of the accessories
    accessories_cost = 0.1 * 3000

    # Calculate the total cost of the purchase
    total_cost = 3000 + accessories_cost

    # Calculate how much money Jeremy had before the purchase
    money_before_purchase = 2 * 3000

    # Calculate how much money Jeremy has left after the purchase
    money_after_purchase = money_before_purchase - total_cost

    # Display how much money Jeremy has left
    result = money_after_purchase
    return result

print(solution())