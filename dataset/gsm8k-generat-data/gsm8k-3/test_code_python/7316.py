def solution():
    """Phillip wants to make pickles with the supplies he finds at home. He has 4 jars, 10 cucumbers, and 100 oz of vinegar. Each cucumber makes six pickles. Each jar can hold 12 pickles. It takes 10 ounces of vinegar per jar of pickles. When he is all done making as many pickles as he has supplies for, how many ounces of vinegar are left?"""
    
    # Calculate the total number of pickles he can make with the cucumbers
    total_pickles = 10 * 6

    # Calculate the total number of jars he will need
    jars_needed = total_pickles // 12

    # Calculate the total amount of vinegar needed
    vinegar_needed = jars_needed * 10

    # Determine how much vinegar is left
    vinegar_left = 100 - vinegar_needed

    # Display the amount of vinegar left
    result = vinegar_left
    return result

print(solution())