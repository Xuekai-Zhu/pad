def solution():
    cleaner_per_dog = 6
    cleaner_per_cat = 4
    cleaner_per_rabbit = 1

    num_dogs = 6
    num_cats = 3
    num_rabbits = 1

    # Calculate the total amount of cleaner needed for all dogs
    total_cleaner_dogs = num_dogs * cleaner_per_dog

    # Calculate the total amount of cleaner needed for all cats
    total_cleaner_cats = num_cats * cleaner_per_cat

    # Calculate the total amount of cleaner needed for all rabbits
    total_cleaner_rabbits = num_rabbits * cleaner_per_rabbit

    # Calculate the total amount of cleaner needed to clean up all stains
    total_cleaner_needed = total_cleaner_dogs + total_cleaner_cats + total_cleaner_rabbits
    result = total_cleaner_needed
    return result

print(solution())