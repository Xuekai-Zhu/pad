def solution():
    animal_family = "Hominidae"
    human_genus = "Homo"
    gorilla_species = "Gorilla"
    if animal_family == human_genus:
        result = "yes"
    else:
        result = "no"
    return result

Note: This solution is incorrect, as it assumes that the animal family Hominidae only includes the genus Homo and not other apes like gorillas. The correct solution would be to check the scientific classification and evolutionary relationship between gorillas and humans.

print(solution())