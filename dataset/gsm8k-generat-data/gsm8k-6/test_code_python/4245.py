def solution():
    # Calculate the number of animals hunted in a day
    animals_Sam = 6
    animals_Rob = animals_Sam / 2
    animals_total_Rob_Sam = animals_Sam + animals_Rob
    animals_Mark = (1/3) * animals_total_Rob_Sam
    animals_Peter = 3 * animals_Mark
    total_animals = animals_Sam + animals_Rob + animals_Mark + animals_Peter
    result = total_animals
    return result

print(solution())