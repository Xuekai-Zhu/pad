def solution():
    total_dishes = 10  # total number of dishes on the menu
    
    dishes_with_bl = 2 + 2  # dishes with beans and lentils, and dishes with beans and seitan
    dishes_with_one = total_dishes - dishes_with_bl  # dishes with only one kind of protein
    
    beans_only = dishes_with_one / 2  # half of the remaining dishes have only beans
    seitan_only = beans_only / 3  # there are three times as many dishes with only beans as with only seitan
    
    lentils_dishes = dishes_with_bl - (beans_only + seitan_only)  # dishes that include lentils
    
    result = lentils_dishes
    return result

print(solution())