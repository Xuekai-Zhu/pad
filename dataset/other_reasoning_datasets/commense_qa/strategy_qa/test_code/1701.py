def solution():
    bald_eagles_on_earth = True
    mount_sharp_on_mars = True
    no_life_on_mars = True
    if bald_eagles_on_earth and not mount_sharp_on_mars and not no_life_on_mars:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())