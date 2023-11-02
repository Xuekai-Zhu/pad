def solution():
    sam_german_shepherds = 3
    sam_french_bulldogs = 4
    peter_german_shepherds = 3 * sam_german_shepherds
    peter_french_bulldogs = 2 * sam_french_bulldogs

    # Calculate the total number of dogs Peter wants to have
    total_dogs = peter_german_shepherds + peter_french_bulldogs
    result = total_dogs
    return result

print(solution())