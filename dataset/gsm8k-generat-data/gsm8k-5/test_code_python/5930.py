def solution():
    cleaner_per_dog = 6  # Marcy uses 6 ounces of cleaner per dog
    cleaner_per_cat = 4  # Marcy uses 4 ounces of cleaner per cat
    cleaner_per_rabbit = 1  # Marcy uses 1 ounce of cleaner per rabbit
    num_dogs = 6  # Marcy needs to clean up after 6 dogs
    num_cats = 3  # Marcy needs to clean up after 3 cats
    num_rabbits = 1  # Marcy needs to clean up after 1 rabbit

    # Calculate the total amount of cleaner needed
    total_cleaner = (cleaner_per_dog * num_dogs) + (cleaner_per_cat * num_cats) + (cleaner_per_rabbit * num_rabbits)
    result = total_cleaner
    return result

print(solution())