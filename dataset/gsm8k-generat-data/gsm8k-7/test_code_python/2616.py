def solution():
    shop_a_bottles = 150
    shop_b_bottles = 180
    total_bottles = 550

    # Calculate the total number of bottles bought from shop A and shop B combined
    total_a_b_bottles = shop_a_bottles + shop_b_bottles

    # Calculate the number of bottles bought from shop C
    shop_c_bottles = total_bottles - total_a_b_bottles
    result = shop_c_bottles
    return result

print(solution())