def solution():
    total_dishes = 10
    bean_lentil_dishes = 2
    bean_seitan_dishes = 2

    # Calculate the number of dishes with only one kind of protein
    one_protein_dishes = total_dishes - bean_lentil_dishes - bean_seitan_dishes

    # Calculate the number of dishes with only beans
    bean_dishes = one_protein_dishes / 2

    # Calculate the number of dishes with only seitan
    seitan_dishes = bean_dishes / 3

    # Calculate the number of dishes with only lentils
    lentil_dishes = total_dishes - bean_lentil_dishes - bean_seitan_dishes - bean_dishes - seitan_dishes
    
    result = lentil_dishes
    return result

print(solution())