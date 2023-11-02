def solution():
    mount_sharp_on_mars = True
    apollo_15_landed_on_moon = True
    if not apollo_15_landed_on_moon and mount_sharp_on_mars:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())