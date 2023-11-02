def solution():
    """A vegan restaurant serves three kinds of protein: seitan, beans, and lentils. There are ten dishes on their menu.
    Two have beans and lentils, and two have beans and seitan. The remaining dishes only have one kind of protein in them.
    Half of the remaining dishes have only beans, and there are three times as many dishes with only beans as with only seitan.
    How many dishes include lentils?"""
    total_dishes = 10
    beans_lentils = 2
    beans_seitan = 2
    one_protein = total_dishes - beans_lentils - beans_seitan
    beans_only = one_protein / 2
    seitan_only = beans_only / 3
    lentils = beans_lentils
    result = lentils
    return result

print(solution())