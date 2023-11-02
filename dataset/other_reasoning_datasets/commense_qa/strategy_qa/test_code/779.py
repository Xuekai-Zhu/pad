def solution():
    headquarters_location = "Shiodome City Center, Minato ward, Tokyo"
    is_metropolitan_area = True
    has_bodies_of_water = False
    if is_metropolitan_area and not has_bodies_of_water:
        result = "no"
    else:
        result = "not enough information"
    return result

print(solution())