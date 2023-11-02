def solution():
    """Raphael went to buy some school supplies. He bought 4 pens which cost $1.5 each, 2 notebooks which cost $4 each, and a rim of bond paper which cost $20. How much did Raphael spend on everything?"""
    pens = 4
    pens_cost = 1.5
    notebooks = 2
    notebook_cost = 4
    bond_paper = 20
    total_cost = (pens * pens_cost) + (notebooks * notebook_cost) + bond_paper
    result = total_cost
    return result

print(solution())