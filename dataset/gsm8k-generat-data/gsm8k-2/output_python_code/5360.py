def solution():
    """A restaurant buffet has 36 different dishes available to try. The restaurant features mango salsa on three of its dishes, fresh mangoes in a sixth of its dishes, and mango jelly in one dish. Oliver despises mangoes and won't eat them, but can pick them out of two of the dishes with fresh mango that he would be willing to try. How many dishes are left for Oliver on the buffet?"""
    mango_salsa_dishes = 3
    fresh_mango_dishes = 36 // 6
    mango_jelly_dishes = 1
    mango_dishes = mango_salsa_dishes + fresh_mango_dishes + mango_jelly_dishes
    dishes_with_fresh_mango = fresh_mango_dishes - 2
    dishes_left = 36 - mango_dishes - dishes_with_fresh_mango
    result = dishes_left
    return result

print(solution())