def solution():
    """At the zoo, there are 5 different types of animals. Seeing each animal type takes around 6 minutes. How much time would it take to see each animal type if the zoo decided to import 4 new species?"""
    animal_types = 5
    minutes_per_type = 6
    new_species = 4
    total_animal_types = animal_types + new_species
    total_time = total_animal_types * minutes_per_type
    result = total_time
    return result

print(solution())