def solution():
    
    giraffes = 5
    penguins = giraffes * 2
    penguins_percentage = 20
    total_animals = (penguins / (penguins_percentage / 100))
    elephants_percentage = 4
    elephants = total_animals * (elephants_percentage / 100)
    result = elephants
    return result

print(solution())