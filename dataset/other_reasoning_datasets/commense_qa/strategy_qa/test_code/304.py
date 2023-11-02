def solution():
    artillery_weapons = ["howitzers", "mortars", "rockets"]
    max_mortar_range = 4680
    slingshot_max_range = 9
    if "slingshot" in artillery_weapons or slingshot_max_range >= max_mortar_range:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())