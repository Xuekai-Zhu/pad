def solution():
    first_cat_frequency = 3
    second_cat_frequency = 2 * first_cat_frequency
    third_cat_frequency = second_cat_frequency / 3
    total_time = 5

    # Calculate the total number of meows by the first cat in 5 minutes
    first_cat_meows = first_cat_frequency * total_time

    # Calculate the total number of meows by the second cat in 5 minutes
    second_cat_meows = second_cat_frequency * total_time

    # Calculate the total number of meows by the third cat in 5 minutes
    third_cat_meows = third_cat_frequency * total_time

    # Calculate the combined total number of meows by all three cats in 5 minutes
    total_meows = first_cat_meows + second_cat_meows + third_cat_meows
    result = total_meows
    return result

print(solution())