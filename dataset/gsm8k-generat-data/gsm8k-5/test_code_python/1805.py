def solution():
    initial_doves = 20  # Giselle had 20 female doves
    eggs_laid = initial_doves * 3  # Each dove laid 3 eggs
    eggs_hatched = eggs_laid * 3/4  # 3/4 of the eggs hatched
    new_doves = eggs_hatched + initial_doves  # The hatched eggs became new doves
    result = new_doves
    return result

print(solution())