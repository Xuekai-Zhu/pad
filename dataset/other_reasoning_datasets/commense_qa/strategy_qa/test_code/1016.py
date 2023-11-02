def solution():
    louvre_pyramid_materials = ["glass", "metal"]
    louvre_pyramid_glass_thickness = 10
    is_glass_unbreakable = False
    if louvre_pyramid_materials.count("glass") > 0:
        if louvre_pyramid_glass_thickness < 20:
            is_glass_unbreakable = False
        else:
            is_glass_unbreakable = True
    if is_glass_unbreakable:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())