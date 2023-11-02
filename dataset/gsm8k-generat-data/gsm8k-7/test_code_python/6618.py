def solution():
    num_jackets_bought = 4
    num_tshirts_bought = 9

    # Calculate the number of free jackets that Martha will get
    num_free_jackets = num_jackets_bought // 2

    # Calculate the number of free t-shirts that Martha will get
    num_free_tshirts = num_tshirts_bought // 3

    # Calculate the total number of clothes that Martha will take home
    total_clothes = num_jackets_bought + num_tshirts_bought + num_free_jackets + num_free_tshirts
    result = total_clothes
    return result

print(solution())