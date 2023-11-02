def solution():
    """Blake gave some of his money to his friend, Connie. Connie used all the money she had been given to buy some land. In one year, the land tripled in value. So, she sold the land and gave half of all the money she got from the sale of the land to Blake. If Connie gave Blake $30,000, how much money, in dollars, did Blake initially give to Connie?"""
    
    # Since Connie gave half of the money from the sale of the land to Blake, this means Blake received a total of $60,000.
    # Let X be the amount of money that Blake initially gave to Connie.
    # After the land tripled in value, Connie received 3X dollars from selling the land.
    # Therefore, we have: 
    # 3X / 2 = $60,000
    # Solving for X, we get:
    initial_amount = 40000
    
    result = initial_amount
    return result

print(solution())