def solution():
    num_apples = 64
    num_baskets = 4
    apples_per_basket_before = num_apples / num_baskets
    apples_taken_by_sister = 3
    apples_per_basket_after = apples_per_basket_before - apples_taken_by_sister
    result = apples_per_basket_after
    return result

print(solution())