def solution():
    """Wanda has 62 crayons. Dina has 28 and Jacob has two fewer crayons than Dina. How many crayons do they have in total?"""
    wanda_crayons = 62
    dina_crayons = 28
    jacob_crayons = dina_crayons - 2
    total_crayons = wanda_crayons + dina_crayons + jacob_crayons
    result = total_crayons
    return result

print(solution())