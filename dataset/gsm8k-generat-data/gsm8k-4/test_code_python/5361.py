def solution():
    """A restaurant buffet has 36 different dishes available to try. The restaurant features mango salsa on three of its dishes, fresh mangoes in a sixth of its dishes, and mango jelly in one dish. Oliver despises mangoes and won't eat them, but can pick them out of two of the dishes with fresh mango that he would be willing to try. How many dishes are left for Oliver on the buffet?"""
    # Define the total number of dishes
    total_dishes = 36

    # Calculate the number of dishes with mango salsa
    mango_salsa_dishes = 3

    # Calculate the number of dishes with fresh mango
    fresh_mango_dishes = total_dishes // 6

    # Calculate the number of dishes with mango jelly
    mango_jelly_dishes = 1

    # Calculate the number of dishes with mango that Oliver won't eat
    unwanted_mango_dishes = 2

    # Calculate the number of dishes left for Oliver on the buffet
    dishes_left = total_dishes - mango_salsa_dishes - fresh_mango_dishes - mango_jelly_dishes - unwanted_mango_dishes

    # return the result
    result = dishes_left
    return result

print(solution())