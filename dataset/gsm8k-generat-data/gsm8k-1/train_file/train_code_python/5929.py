def solution():
    """Marcy uses 6 ounces of pet cleaner to clean up a dog stain, 4 ounces to clean up a cat stain, and 1 ounce to clean up a rabbit stain. How much cleaner does she need to clean up after 6 dogs, 3 cats and 1 rabbit?"""
    dog_cleaner_per_stain = 6
    cat_cleaner_per_stain = 4
    rabbit_cleaner_per_stain = 1
    total_dog_cleaner = dog_cleaner_per_stain * 6
    total_cat_cleaner = cat_cleaner_per_stain * 3
    total_rabbit_cleaner = rabbit_cleaner_per_stain * 1
    total_cleaner = total_dog_cleaner + total_cat_cleaner + total_rabbit_cleaner
    result = total_cleaner
    return result

print(solution())