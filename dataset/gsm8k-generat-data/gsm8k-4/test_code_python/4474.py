def solution():
    """Alison has half as much money as Brittany. Brittany has 4 times as much money as Brooke. 
    Brooke has twice as much money as Kent. If Kent has $1,000, how much money does Alison have?"""
    # Define Kent's initial amount of money
    kent_money = 1000

    # Calculate Brooke's amount of money
    brooke_money = kent_money * 2

    # Calculate Brittany's amount of money
    brittany_money = brooke_money * 4

    # Calculate Alison's amount of money
    alison_money = brittany_money / 2

    # return the result
    result = alison_money
    return result

print(solution())