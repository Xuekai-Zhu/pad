def solution():
    num_daughters = 2
    flowers_per_daughter = 5
    additional_flowers = 20
    dead_flowers = 10
    num_baskets = 5

    # Calculate the total number of flowers planted
    total_planted = num_daughters * flowers_per_daughter

    # Calculate the total number of flowers after additional growth and deaths
    total_grown = total_planted + additional_flowers - dead_flowers

    # Calculate the number of flowers in each basket
    flowers_per_basket = total_grown // num_baskets
    result = flowers_per_basket
    return result

print(solution())