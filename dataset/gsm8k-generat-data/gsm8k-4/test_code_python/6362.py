def solution():
    """Frank spent 1/5 of his money to buy groceries. He then spent 1/4 of the remaining money to buy a magazine. If he had $360 left in his wallet, how much money did he have at first?"""
    # Define the final amount of money
    final_amount = 360
    
    # Calculate the amount of money spent on the magazine
    magazine_spending = final_amount / (1/4)
    
    # Calculate the amount of money remaining after buying the magazine
    remaining_money = magazine_spending / (4/3)
    
    # Calculate the amount of money spent on groceries
    grocery_spending = remaining_money / (4/5)
    
    # Calculate the initial amount of money
    initial_amount = grocery_spending * 5
    
    result = initial_amount
    return result

print(solution())