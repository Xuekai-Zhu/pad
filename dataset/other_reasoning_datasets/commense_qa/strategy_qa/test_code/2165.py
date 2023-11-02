def solution():
    endangered_species = ["Sea Otters"]
    non_mammal_seafood = ["Fish", "Shrimp", "Clams", "Crab"]
    if "Sea Otters" in endangered_species and "Sea Otters" not in non_mammal_seafood:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())