def solution():
    """Phillip wants to make pickles with the supplies he finds at home. He has 4 jars, 10 cucumbers, and 100 oz of vinegar. Each cucumber makes six pickles. Each jar can hold 12 pickles. It takes 10 ounces of vinegar per jar of pickles. When he is all done making as many pickles as he has supplies for, how many ounces of vinegar are left?"""
    jars = 4
    cucumbers = 10
    vinegar = 100
    pickles_per_cucumber = 6
    pickles_per_jar = 12
    vinegar_per_jar = 10
    total_pickles = min(cucumbers * pickles_per_cucumber, jars * pickles_per_jar)
    total_vinegar = total_pickles // pickles_per_jar * vinegar_per_jar
    vinegar_left = vinegar - total_vinegar
    result = vinegar_left
    return result

print(solution())