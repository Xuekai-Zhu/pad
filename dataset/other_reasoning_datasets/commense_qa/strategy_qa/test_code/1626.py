def solution():
    targeted_plants = ["Solanaceae", "eggplant"]
    controlling_species = ["Selenops radiatus"]
    # Check if the controlling species targets the same plant family or plant as the parasite
    if set(targeted_plants) & set(controlling_species):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())