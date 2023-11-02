def solution():
    """Blake gave some of his money to his friend, Connie. Connie used all the money she had been given to buy some land. In one year, the land tripled in value. So, she sold the land and gave half of all the money she got from the sale of the land to Blake. If Connie gave Blake $30,000, how much money, in dollars, did Blake initially give to Connie?"""
    # Let x be the initial amount of money Blake gave to Connie
    # After Connie buys land, the value triples, so Connie now has 3x dollars
    # Connie sells the land and gives half the money, or (3/2)x, to Blake
    # We are given that (3/2)x - x = 30000, which simplifies to x = 60000
    result = 60000
    return result

print(solution())