def solution():
    largest_asteroid_size = "miniature planet"
    mercury_radius = 1516
    city_length = 13.4
    city_width = 2.3
    mercury_weight = 3.285 * (10**23)

    largest_asteroid_weight = mercury_weight * ((largest_asteroid_size/mercury_radius)**3)
    city_area = city_length * city_width

    if largest_asteroid_weight > city_area:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())