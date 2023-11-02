def solution():
    """Wanda has 62 crayons. Dina has 28 and Jacob has two fewer crayons than Dina. How many crayons do they have in total?"""
    # Define the number of crayons each person has
    wanda_crayons = 62
    dina_crayons = 28
    jacob_crayons = dina_crayons - 2

    # Calculate the total number of crayons
    total_crayons = wanda_crayons + dina_crayons + jacob_crayons

    # Display the total number of crayons
    result = total_crayons
    return result

print(solution())