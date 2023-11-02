def solution():
    # Calculate the number of pieces of candy after Boris' daughter eats some
    remaining_candy = 100 - 8  

    # Calculate the number of pieces of candy in each bowl after Boris separates them
    candy_per_bowl = remaining_candy // 4  

    # Calculate the number of pieces of candy in each bowl after Boris takes some for himself
    candy_per_bowl_after_taking = candy_per_bowl - 3  
    result = candy_per_bowl_after_taking
    return result

print(solution())