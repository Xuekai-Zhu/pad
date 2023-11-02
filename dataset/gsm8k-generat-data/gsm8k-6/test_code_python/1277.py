def solution():
    # Calculate the initial number of apples in each basket
    init_apples_per_basket = 64 // 4  # 64 apples divided into 4 baskets
    # Calculate the number of apples in each basket after Jane's sister took 3 from each
    apples_per_basket_now = init_apples_per_basket - 3
    result = apples_per_basket_now
    return result

print(solution())