def solution():
    total_dishes = 36  # The restaurant has 36 different dishes

    # Calculate the number of dishes with mango salsa, fresh mangoes, and mango jelly respectively
    dishes_with_salsa = 3
    dishes_with_fresh_mango = total_dishes // 6
    dishes_with_jelly = 1

    # Calculate the number of dishes that Oliver won't eat due to mangoes
    mango_dishes = 2  # Oliver can pick out mangoes from 2 of the dishes with fresh mango

    # Calculate the number of dishes left for Oliver
    remaining_dishes = total_dishes - (dishes_with_salsa + dishes_with_fresh_mango + dishes_with_jelly + mango_dishes)
    result = remaining_dishes
    return result

print(solution())