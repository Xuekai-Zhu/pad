def solution():
    """Wanda has 62 crayons. Dina has 28 and Jacob has two fewer crayons than Dina. How many crayons do they have in total?"""
    # Define the initial number of crayons
    wanda_crayons = 62
    dina_crayons = 28
    jacob_crayons = dina_crayons - 2

    # Calculate the total number of crayons
    total_crayons = wanda_crayons + dina_crayons + jacob_crayons

    # return the result
    result = total_crayons
    return result

print(solution())