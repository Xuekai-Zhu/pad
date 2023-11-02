def solution():
    snow_leopards_native_to = ["Central Asia", "South Asia"]
    yucatan_location = "Mexico"
    continent = "North America"
    if yucatan_location in snow_leopards_native_to or continent != "Asia":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())