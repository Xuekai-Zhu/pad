def solution():
    """Blake gave some of his money to his friend, Connie. Connie used all the money she had been given to buy some land. In one year, the land tripled in value. So, she sold the land and gave half of all the money she got from the sale of the land to Blake. If Connie gave Blake $30,000, how much money, in dollars, did Blake initially give to Connie?"""
    half_of_sale = 30000
    sale_price = half_of_sale * 2
    initial_value = sale_price / 3
    result = initial_value
    return result

print(solution())