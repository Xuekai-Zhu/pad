def solution():
    total_animals = 20 + 10 + 14
    animals_drowned = 3 + (2 * 10)
    animals_made_it_to_shore = total_animals - animals_drowned
    result = animals_made_it_to_shore
    return result

print(solution())