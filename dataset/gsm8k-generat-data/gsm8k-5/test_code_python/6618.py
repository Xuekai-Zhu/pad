def solution():
    # Calculate the number of free jackets Martha gets
    free_jackets = 4 // 2  # For every 2 jackets, she gets 1 free jacket

    # Calculate the number of free t-shirts Martha gets
    free_tshirts = 9 // 3  # For every 3 t-shirts, she gets 1 free t-shirt

    # Calculate the total number of clothes Martha takes home
    total_clothes = 4 + 9 + free_jackets + free_tshirts

    result = total_clothes
    return result

print(solution())