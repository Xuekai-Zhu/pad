def solution():
    
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