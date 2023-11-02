def solution():
    basketball_diameter = 9.5
    sand_cat_ear_height = 2.8
    # Calculate the radius of the basketball by dividing the diameter by 2
    basketball_radius = basketball_diameter / 2
    # Calculate the maximum diameter of an object that can fit in the sand cat's ear by multiplying the ear height by 2
    max_object_diameter = sand_cat_ear_height * 2
    if basketball_radius <= max_object_diameter:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())