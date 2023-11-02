def solution():
    """Oliver had $9, then he saved $5 from his allowance and spent $4 on a frisbee and $3 on a puzzle. His friend gives him another $8 as it's his birthday. How much money does Oliver have left?"""
    
    # Define Oliver's initial amount of money
    oliver_money = 9
    
    # Add the money he saved and his birthday gift
    oliver_money += 5
    oliver_money += 8
    
    # Subtract the money he spent on the frisbee and puzzle
    oliver_money -= 4
    oliver_money -= 3
    
    # Return the remaining amount of money that Oliver has
    result = oliver_money
    return result

print(solution())