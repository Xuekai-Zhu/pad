def solution():
    first_cat_meows = 3 * 5  # The first cat meows 3 times per minute for 5 minutes
    second_cat_meows = 2 * first_cat_meows  # The second cat meows twice as much as the first cat
    third_cat_meows = second_cat_meows / 3  # The third cat meows at one-third the frequency of the second cat

    # Calculate the total number of meows from all three cats
    total_meows = first_cat_meows + second_cat_meows + third_cat_meows
    result = total_meows
    return result

print(solution())