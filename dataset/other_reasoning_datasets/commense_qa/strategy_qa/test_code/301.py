def solution():
    crustacean_habitats = ["terrestrial", "freshwater", "ocean"]
    ocean_only = False
    if "ocean" in crustacean_habitats:
        ocean_only = False
    else:
        ocean_only = True
    return ocean_only

print(solution())