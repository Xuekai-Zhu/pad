def solution():
    # Calculate the number of tomatoes on the first two plants
    tomatoes_plant1 = 8
    tomatoes_plant2 = tomatoes_plant1 + 4
    total_tomatoes_first2plants = tomatoes_plant1 + tomatoes_plant2

    # Calculate the number of tomatoes on the remaining two plants
    tomatoes_plant3 = 3 * total_tomatoes_first2plants
    tomatoes_plant4 = 3 * total_tomatoes_first2plants
    total_tomatoes_last2plants = tomatoes_plant3 + tomatoes_plant4

    # Calculate the total number of tomatoes
    total_tomatoes = total_tomatoes_first2plants + total_tomatoes_last2plants

    result = total_tomatoes
    return result

print(solution())