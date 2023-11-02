def solution():
    january_animal_sightings = 26
    february_animal_sightings = january_animal_sightings * 3
    march_animal_sightings = february_animal_sightings / 2

    total_animal_sightings = january_animal_sightings + february_animal_sightings + march_animal_sightings
    result = total_animal_sightings
    return result

print(solution())