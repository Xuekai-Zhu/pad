def solution():
    """Phillip wants to make pickles with the supplies he finds at home. He has 4 jars, 10 cucumbers, and 100 oz of vinegar. Each cucumber makes six pickles. Each jar can hold 12 pickles. It takes 10 ounces of vinegar per jar of pickles. When he is all done making as many pickles as he has supplies for, how many ounces of vinegar are left?"""
    # Define the initial supplies
    jars = 4
    cucumbers = 10
    vinegar = 100

    # Calculate the number of pickles that can be made
    pickles = min(cucumbers * 6, jars * 12)

    # Calculate the amount of vinegar used to make the pickles
    vinegar_used = pickles // 12 * 10

    # Calculate the amount of vinegar left
    vinegar_left = vinegar - vinegar_used

    # Return the result
    result = vinegar_left
    return result

print(solution())