def solution():
    cinnamon_type = "Indonesian"
    spice_grinder_useful = True
    if cinnamon_type == "Indonesian":
        spice_grinder_useful = False
    if spice_grinder_useful == True:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())