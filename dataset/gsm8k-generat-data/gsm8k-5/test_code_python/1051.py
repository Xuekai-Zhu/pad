def solution():
    reptile_house_animals = 16  # The Reptile House has 16 animals
    rain_forest_animals = (reptile_house_animals + 5) / 3  # The Reptile House has 5 fewer animals than 3 times the number of animals in the Rain Forest exhibit

    # Round up the number of animals in the Rain Forest exhibit to the nearest whole number
    rain_forest_animals = int(rain_forest_animals + 0.5)

    result = rain_forest_animals
    return result

print(solution())