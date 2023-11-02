def solution():
    bucharest_location = "Eastern Europe"
    egypt_location = "Africa"
    africa_is_south_of_europe = True
    if bucharest_location == "Eastern Europe" and egypt_location == "Africa" and africa_is_south_of_europe:
        result = "no"
    else:
        result = "not applicable"
    return result

print(solution())