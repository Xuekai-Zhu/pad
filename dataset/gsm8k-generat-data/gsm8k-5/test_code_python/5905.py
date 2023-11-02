def solution():
    total_dishes = 10

    # Calculate the number of dishes with beans and lentils or beans and seitan
    dishes_with_bl = 2
    dishes_with_bs = 2
    total_dishes_with_blbs = dishes_with_bl + dishes_with_bs

    # Calculate the number of dishes with only one kind of protein
    dishes_with_one_protein = total_dishes - total_dishes_with_blbs

    # Calculate the number of dishes with only beans
    beans_dishes = dishes_with_one_protein / 2
    seitan_dishes = beans_dishes / 3

    # Calculate the number of dishes with only lentils
    lentils_dishes = dishes_with_one_protein - beans_dishes - seitan_dishes

    result = lentils_dishes
    return result

print(solution())