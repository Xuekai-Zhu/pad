def solution():
    """Blake gave some of his money to his friend, Connie.  Connie used all the money she had been given to buy some land.  In one year, the land tripled in value.  So, she sold the land and gave half of all the money she got from the sale of the land to Blake.  If Connie gave Blake $30,000, how much money, in dollars, did Blake initially give to Connie?"""
    
    # Let the amount of money Blake initially gave to Connie be x
    # After buying the land, its value tripled in one year, so its new value was 3 times its original value, which is 3x
    # Connie sold the land and gave half of the money she got to Blake, which is (1/2) * 3x = (3/2)x
    # We know that (3/2)x = $30,000, so solving for x gives x = $20,000
    
    initial_amount = 20000
    
    # Display the initial amount of money that Blake gave to Connie
    result = initial_amount
    return result

print(solution())