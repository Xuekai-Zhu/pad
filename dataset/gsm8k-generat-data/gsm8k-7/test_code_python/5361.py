def solution():
    total_dishes = 36

    # Calculate the number of dishes with mango salsa
    mango_salsa_dishes = 3

    # Calculate the number of dishes with fresh mango
    fresh_mango_dishes = total_dishes // 6

    # Calculate the number of dishes with mango jelly
    mango_jelly_dishes = 1

    # Calculate the total number of dishes with mango
    total_mango_dishes = mango_salsa_dishes + fresh_mango_dishes + mango_jelly_dishes

    # Calculate the number of dishes that Oliver won't eat because of mango
    mango_restricted_dishes = 2

    # Calculate the number of dishes left for Oliver
    dishes_left = total_dishes - total_mango_dishes - mango_restricted_dishes

    result = dishes_left
    return result

print(solution())