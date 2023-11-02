def solution():
    
    initial_animals = 68
    gorilla_family = 6
    hippo = 1
    rhinos = 3
    meerkats = 0
    lion_cubs = 0

    
    current_animals = initial_animals - gorilla_family + hippo + rhinos + lion_cubs + meerkats

    
    while current_animals != 90:
        lion_cubs += 1
        meerkats = 2 * lion_cubs
        current_animals = initial_animals - gorilla_family + hippo + rhinos + lion_cubs + meerkats

    result = lion_cubs
    return result

print(solution())