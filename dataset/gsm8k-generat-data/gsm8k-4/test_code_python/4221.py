def solution():
    """John goes to the market with €100. He buys a roast for €17 and vegetables for €11. How much money does he have left?"""
    # Define the initial amount of money John has
    initial_money = 100
    
    # Define the amount of money John spends on the roast and vegetables
    roast_price = 17
    vegetables_price = 11
    
    # Calculate the amount of money John has left
    money_left = initial_money - roast_price - vegetables_price
    
    # Return the result
    return money_left

print(solution())