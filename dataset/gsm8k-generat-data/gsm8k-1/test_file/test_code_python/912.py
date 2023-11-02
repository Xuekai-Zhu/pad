def solution():
    """Julia and Nadine were given the same amount of allowance by their mother. 
    The two girls decided to combine their allowance to surprise their father on his birthday. 
    They bought a cake which costs $11. They also bought 1 dozen balloons which were sold for $0.5 for 2 balloons. 
    The remaining money was used to buy 2 tubs of ice cream for $7 each. 
    How much did Julia and Nadine's mother give each one of them?"""
    
    total_spent = 11 + (6 * 0.5) + (2 * 7) # Cake + balloons + ice cream
    remaining_money = total_money - total_spent
    allowance_each = remaining_money / 2
    
    result = allowance_each
    return result

print(solution())