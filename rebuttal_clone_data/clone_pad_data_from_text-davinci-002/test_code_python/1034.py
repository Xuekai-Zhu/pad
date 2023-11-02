def solution():
    
    cups_of_sugar = 2
    cream_cheese_to_sugar_ratio = 4
    cups_of_cream_cheese = cups_of_sugar / cream_cheese_to_sugar_ratio
    teaspoons_of_vanilla = cups_of_cream_cheese * (1 / 2)
    eggs_per_teaspoon_of_vanilla = 2
    total_eggs = teaspoons_of_vanilla * eggs_per_teaspoon_of_vanilla
    result = total_eggs
    return result

print(solution())