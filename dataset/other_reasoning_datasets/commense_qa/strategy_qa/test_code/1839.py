def solution():
    coffee_climates = ["subtropical", "equatorial"]
    new_england_climate = "humid continental"
    if new_england_climate in coffee_climates:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())