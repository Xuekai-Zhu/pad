def solution():
    # Calculate the total number of legs of Daniel's animals
    horse_legs = 2 * 4  # 2 horses with 4 legs each
    dog_legs = 5 * 4  # 5 dogs with 4 legs each
    cat_legs = 7 * 4  # 7 cats with 4 legs each
    turtle_legs = 3 * 4  # 3 turtles with 4 legs each
    goat_legs = 1 * 4  # 1 goat with 4 legs
    total_legs = horse_legs + dog_legs + cat_legs + turtle_legs + goat_legs  # sum of legs of all animals
    result = total_legs
    return result

print(solution())