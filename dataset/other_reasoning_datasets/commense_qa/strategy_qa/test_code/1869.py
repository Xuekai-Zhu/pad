def solution():
    # Define the animals that produce silk
    silk_producing_animals = ["spiders", "beetles", "caterpillars", "fleas"]
    # Check if Bombyx mori is the exclusive supplier of silk
    if "Bombyx mori" in silk_producing_animals and len(silk_producing_animals)==1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())