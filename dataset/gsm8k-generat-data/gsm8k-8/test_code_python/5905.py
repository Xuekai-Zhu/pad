def solution():
    # Define the number of dishes with each protein
    beans = 0
    seitan = 0
    lentils = 0

    # Calculate the number of dishes with only beans and only seitan
    beans_only = 10 // 2 // 2
    seitan_only = beans_only // 3

    # Calculate the number of dishes with lentils
    lentils = 10 - (2 + 2 + beans_only + seitan_only)
    
    result = lentils
    return result

print(solution())