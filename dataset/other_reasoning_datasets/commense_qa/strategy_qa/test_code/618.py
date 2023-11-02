def solution():
    passion_tea_flavors = ["cinnamon", "apple", "licorice root", "lemongrass"]
    ginger = "ginger"
    if ginger in passion_tea_flavors:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())