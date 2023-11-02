def solution():
    """Cathy has $12 left in her wallet. Her dad sent her $25 for her weekly consumption while her mom sent her twice the amount her dad sent her. How much money does Cathy have now?"""
    
    # Define the amount of money Cathy had initially
    initial_money = 12
    
    # Define the amount of money Cathy's dad sent her
    dad_money = 25
    
    # Define the amount of money Cathy's mom sent her
    mom_money = 2 * dad_money
    
    # Calculate the total amount of money Cathy has now
    total_money = initial_money + dad_money + mom_money
    
    # Display the total amount of money Cathy has now
    result = total_money
    return result

print(solution())