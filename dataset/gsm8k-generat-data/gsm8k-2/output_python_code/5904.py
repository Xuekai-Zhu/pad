def solution():
    """A vegan restaurant serves three kinds of protein: seitan, beans, and lentils. There are ten dishes on their menu. Two have beans and lentils, and two have beans and seitan. The remaining dishes only have one kind of protein in them. Half of the remaining dishes have only beans, and there are three times as many dishes with only beans as with only seitan. How many dishes include lentils?"""
    total_dishes = 10
    beans_and_lentils = 2
    beans_and_seitan = 2
    dishes_with_one_kind_of_protein = total_dishes - beans_and_lentils - beans_and_seitan
    beans_only = dishes_with_one_kind_of_protein / 2
    seitan_only = beans_only / 3
    lentils_only = dishes_with_one_kind_of_protein - beans_only - seitan_only
    dishes_with_lentils = beans_and_lentils + lentils_only
    result = dishes_with_lentils
    return result

print(solution())