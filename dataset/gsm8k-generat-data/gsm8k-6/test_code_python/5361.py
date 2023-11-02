def solution():
    # Calculate the number of dishes featuring mango salsa
    mango_salsa = 3  

    # Calculate the number of dishes with fresh mango
    fresh_mango = 36/6  

    # Calculate the total number of dishes featuring mango
    total_mango = mango_salsa + fresh_mango + 1  # add the dish with mango jelly

    # Calculate the number of dishes with fresh mango that Oliver won't eat
    mango_in_fresh_mango_dishes = 2  

    # Calculate the number of dishes left for Oliver
    dishes_left = 36 - total_mango - mango_in_fresh_mango_dishes  

    result = dishes_left
    return result

print(solution())