def solution():
    """Teresa is collecting pencils. She has 14 colored pencils and 35 black pencils. Her three younger siblings need pencils for class and their dad asks her to share all her pencils, giving each an equal number of pencils, regardless of color. He tells her she can keep 10 of them for herself. How many pencils does each sibling get?"""
    colored_pencils = 14
    black_pencils = 35
    total_pencils = colored_pencils + black_pencils
    num_siblings = 3
    pencils_to_share = total_pencils - 10
    pencils_per_sib = pencils_to_share / num_siblings
    result = pencils_per_sib
    return result

print(solution())