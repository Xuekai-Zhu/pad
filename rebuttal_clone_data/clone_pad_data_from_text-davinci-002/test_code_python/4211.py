def solution():
    basket_a = 15
    basket_b = 30
    basket_c = 20
    basket_d = 25
    total_fruits = basket_a + basket_b + basket_c + basket_d
    average_fruits = total_fruits / 5
    basket_e = average_fruits
    result = basket_e - (basket_a + basket_b + basket_c + basket_d)
    return result

print(solution())