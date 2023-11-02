def solution():
    mitsubishi_plant_location = "Catalao, Brazil"
    distance_to_uberlandia = 70 # in miles

    if distance_to_uberlandia <= 70:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())