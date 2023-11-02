def solution():
    """In January the families visiting a national park see animals 26 times. In February the families that visit the national park see animals three times as many as were seen there in January. Then in March the animals are shyer and the families who visit the national park see animals half as many times as they were seen in February. How many times total did families see an animal in the first three months of the year?"""
    january_animals = 26
    february_animals = 3 * january_animals
    march_animals = february_animals / 2
    total_animals = january_animals + february_animals + march_animals
    result = total_animals
    return result

print(solution())