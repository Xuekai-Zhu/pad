def solution():
    # Calculate Alice's new amount of money after doubling it in the stock market
    alice_money = 2000 * 2  

    # Calculate Bob's new amount of money after making 5 times what he invested in real estate
    bob_money = 2000 + (2000 * 5)  

    # Calculate the difference between Bob and Alice's new amounts of money
    money_difference = bob_money - alice_money  
    result = money_difference
    return result

print(solution())