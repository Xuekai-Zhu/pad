def solution():
    """Colby harvested his mango trees, the total mangoes he harvested is 60 kilograms. He sold 20 kilograms to the market and sold the remaining half to his community. If each kilogram contains 8 mangoes, how many mangoes does he still have?"""
    total_mangoes = 60 * 8
    sold_mangoes = 20 * 8
    remaining_mangoes = (total_mangoes - sold_mangoes) / 2
    result = remaining_mangoes
    return result

print(solution())