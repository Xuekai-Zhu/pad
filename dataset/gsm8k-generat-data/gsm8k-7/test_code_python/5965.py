def solution():
    num_horses = 2
    num_dogs = 5
    num_cats = 7
    num_turtles = 3
    num_goats = 1

    # Calculate the total number of legs for all horses
    total_horse_legs = num_horses * 4

    # Calculate the total number of legs for all dogs
    total_dog_legs = num_dogs * 4

    # Calculate the total number of legs for all cats
    total_cat_legs = num_cats * 4

    # Calculate the total number of legs for all turtles
    total_turtle_legs = num_turtles * 4

    # Calculate the total number of legs for all goats
    total_goat_legs = num_goats * 4

    # Calculate the total number of legs for all animals
    total_legs = total_horse_legs + total_dog_legs + total_cat_legs + total_turtle_legs + total_goat_legs
    result = total_legs
    return result

print(solution())