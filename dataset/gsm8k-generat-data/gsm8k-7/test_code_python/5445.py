def solution():
    miles_to_school = 15
    miles_to_park = 6
    miles_to_restaurant = 2
    miles_to_friend = 4
    miles_home = 11
    miles_driven = miles_to_school + miles_to_park + miles_to_restaurant + miles_to_friend + miles_home
    miles_per_gallon = 19
    gallons_of_gas = miles_driven / miles_per_gallon
    result = gallons_of_gas
    return result

print(solution())