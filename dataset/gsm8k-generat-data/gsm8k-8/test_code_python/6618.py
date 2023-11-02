def solution():
    # Calculate the number of free jackets Martha gets with 4 purchased jackets
    jackets = 4
    free_jackets = jackets // 2

    # Calculate the number of free t-shirts Martha gets with 9 purchased t-shirts
    tshirts = 9
    free_tshirts = tshirts // 3

    # Calculate the total number of jackets and t-shirts Martha takes home
    total_jackets = jackets + free_jackets
    total_tshirts = tshirts + free_tshirts

    # Calculate the final result
    result = total_jackets + total_tshirts
    return result

print(solution())