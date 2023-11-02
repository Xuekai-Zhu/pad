def solution():
    """A vegan restaurant serves three kinds of protein: seitan, beans, and lentils. There are ten dishes on their menu. Two have beans and lentils, and two have beans and seitan. The remaining dishes only have one kind of protein in them. Half of the remaining dishes have only beans, and there are three times as many dishes with only beans as with only seitan. How many dishes include lentils?"""
    # Define the number of dishes on the menu
    total_dishes = 10

    # Define the number of dishes that have both beans and lentils
    beans_lentils_dishes = 2

    # Define the number of dishes that have both beans and seitan
    beans_seitan_dishes = 2

    # Calculate the number of dishes that have only one kind of protein
    one_protein_dishes = total_dishes - beans_lentils_dishes - beans_seitan_dishes

    # Calculate the number of dishes that have only beans
    beans_dishes = one_protein_dishes / 2

    # Calculate the number of dishes that have only seitan
    seitan_dishes = beans_dishes / 3

    # Calculate the number of dishes that include lentils
    lentils_dishes = beans_lentils_dishes

    result = lentils_dishes
    return result

print(solution())