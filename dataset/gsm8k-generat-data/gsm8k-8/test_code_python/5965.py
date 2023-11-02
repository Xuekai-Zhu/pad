def solution():
    # Define the number of legs for each type of animal
    horse_legs = 4
    dog_legs = 4
    cat_legs = 4
    turtle_legs = 4
    goat_legs = 4

    # Calculate the total number of legs for each type of animal
    total_horse_legs = 2 * horse_legs
    total_dog_legs = 5 * dog_legs
    total_cat_legs = 7 * cat_legs
    total_turtle_legs = 3 * turtle_legs
    total_goat_legs = 1 * goat_legs

    # Calculate the total number of legs for all animals
    total_legs = total_horse_legs + total_dog_legs + total_cat_legs + total_turtle_legs + total_goat_legs
    result = total_legs
    return result

print(solution())