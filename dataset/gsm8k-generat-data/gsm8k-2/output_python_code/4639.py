def solution():
    """Teresa is collecting pencils. She has 14 colored pencils and 35 black pencils.
    Her three younger siblings need pencils for class and their dad asks her to share
    all her pencils, giving each an equal number of pencils, regardless of color.
    He tells her she can keep 10 of them for herself. How many pencils does each sibling get?"""
    colored_pencils = 14
    black_pencils = 35
    total_pencils = colored_pencils + black_pencils
    remaining_pencils = total_pencils - 10
    siblings = 3
    pencils_per_sibling = remaining_pencils // siblings
    result = pencils_per_sibling
    return result

print(solution())