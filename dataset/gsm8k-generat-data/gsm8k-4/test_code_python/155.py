def solution():
    """Colby harvested his mango trees, the total mangoes he harvested is 60 kilograms. He sold 20 kilograms to the market and sold the remaining half to his community. If each kilogram contains 8 mangoes, how many mangoes does he still have?"""
    # Define the total mangoes harvested
    total_mangoes = 60 * 8

    # Define the mangoes sold at the market
    market_mangoes = 20 * 8

    # Define the mangoes sold to the community
    community_mangoes = (total_mangoes - market_mangoes) / 2

    # Calculate the remaining mangoes
    remaining_mangoes = total_mangoes - market_mangoes - community_mangoes

    # return the result
    result = remaining_mangoes
    return result

print(solution())