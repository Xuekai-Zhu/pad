def solution():
    """Phillip wants to make pickles with the supplies he finds at home. He has 4 jars, 10 cucumbers, and 100 oz of vinegar. Each cucumber makes six pickles. Each jar can hold 12 pickles. It takes 10 ounces of vinegar per jar of pickles. When he is all done making as many pickles as he has supplies for, how many ounces of vinegar are left?"""
    total_pickles = min(4*12, 10*6)
    jars_needed = (total_pickles+11) // 12
    vinegar_needed = jars_needed * 10
    vinegar_left = max(0, 100 - vinegar_needed)
    result = vinegar_left
    return result

print(solution())