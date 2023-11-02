def solution():
    # Calculate the number of pieces of candy in each bag
    candy_per_bag = 63/9  

    # Calculate the total number of chocolate pieces
    total_chocolate = 2 + 3  

    # Calculate the total number of non-chocolate pieces
    total_non_chocolate = 9 - total_chocolate  

    # Calculate the total number of non-chocolate pieces of candy
    non_chocolate_candy = total_non_chocolate * candy_per_bag  
    result = non_chocolate_candy
    return result

print(solution())