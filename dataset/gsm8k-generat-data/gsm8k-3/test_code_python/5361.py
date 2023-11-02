def solution():
    """A restaurant buffet has 36 different dishes available to try. The restaurant features mango salsa on three of its dishes, fresh mangoes in a sixth of its dishes, and mango jelly in one dish. Oliver despises mangoes and won't eat them, but can pick them out of two of the dishes with fresh mango that he would be willing to try. How many dishes are left for Oliver on the buffet?"""

    # Define the number of dishes with mango salsa, fresh mango, and mango jelly
    mango_salsa = 3
    fresh_mango = 36 // 6
    mango_jelly = 1

    # Calculate the total number of dishes with mango
    total_mango = mango_salsa + fresh_mango + mango_jelly

    # Calculate the number of dishes without mango
    dishes_without_mango = 36 - total_mango

    # Calculate the number of dishes Oliver can try
    dishes_oliver_can_try = dishes_without_mango - 2

    # Display the number of dishes Oliver can try
    result = dishes_oliver_can_try
    return result

print(solution())