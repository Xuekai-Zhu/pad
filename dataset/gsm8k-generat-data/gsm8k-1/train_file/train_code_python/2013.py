def solution():
    """Jennifer is building tanks to hold her goldfish. She built 3 tanks that will hold 15 fish each, heated, and filled them. She plans to build the rest of the tanks equipped with heaters, and they will hold 10 fish each. If she needs to build enough tanks to house a total of 75 fish, how many more will she need to build?"""
    tanks_with_heaters = 3
    fish_per_tank_with_heater = 15
    tanks_without_heaters = (75 - (tanks_with_heaters * fish_per_tank_with_heater)) / 10
    result = tanks_without_heaters
    return result

print(solution())