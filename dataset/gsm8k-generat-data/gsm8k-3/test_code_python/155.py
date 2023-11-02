def solution():
    """Colby harvested his mango trees, the total mangoes he harvested is 60 kilograms. He sold 20 kilograms to the market and sold the remaining half to his community. If each kilogram contains 8 mangoes, how many mangoes does he still have?"""
    # Define the total amount of mangoes harvested
    total_mangoes = 60

    # Define the amount of mangoes sold to the market
    mangoes_market = 20

    # Calculate the amount of mangoes sold to the community
    mangoes_community = (total_mangoes - mangoes_market) / 2

    # Calculate the total amount of mangoes remaining
    mangoes_remaining = total_mangoes - mangoes_market - mangoes_community

    # Calculate the total number of mangoes remaining in terms of individual mangoes
    mango_count = mangoes_remaining * 8

    # return the result
    result = mango_count
    return result

print(solution())