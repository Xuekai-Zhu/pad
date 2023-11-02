def solution():
    # Calculate the total number of clothes Martha will get
    jackets = 4  # number of jackets Martha buys
    free_jackets = jackets // 2  # number of free jackets Martha gets
    t_shirts = 9  # number of t-shirts Martha buys
    free_t_shirts = t_shirts // 3  # number of free t-shirts Martha gets
    total_clothes = jackets + t_shirts + free_jackets + free_t_shirts  # total number of clothes Martha will take home
    result = total_clothes
    return result

print(solution())