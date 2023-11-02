def solution():
    
    first_cat_rate = 3
    second_cat_rate = 2 * first_cat_rate
    third_cat_rate = second_cat_rate / 3
    total_meows = (first_cat_rate + second_cat_rate + third_cat_rate) * 5
    result = total_meows
    return result

print(solution())