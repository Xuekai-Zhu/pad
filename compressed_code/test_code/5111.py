def solution():
    
    jackets_bought = 4
    tshirts_bought = 9
    free_jackets = jackets_bought // 2
    free_tshirts = tshirts_bought // 3
    total_jackets = jackets_bought + free_jackets
    total_tshirts = tshirts_bought + free_tshirts
    result = total_jackets + total_tshirts
    return result

print(solution())