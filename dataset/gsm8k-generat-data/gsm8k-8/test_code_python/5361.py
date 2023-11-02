def solution():
    total_dishes = 36
    mango_salsa_dishes = 3
    fresh_mango_dishes = total_dishes // 6
    mango_jelly_dishes = 1

    dishes_with_mango = mango_salsa_dishes + fresh_mango_dishes + mango_jelly_dishes
    dishes_without_mango = total_dishes - dishes_with_mango

    dishes_available_for_oliver = dishes_without_mango - 2
    result = dishes_available_for_oliver
    return result

print(solution())