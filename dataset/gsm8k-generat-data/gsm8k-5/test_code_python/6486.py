def solution():
    distance_to_dermatologist = 30
    distance_to_gynecologist = 50
    total_distance = (distance_to_dermatologist + distance_to_gynecologist) * 2  # She has to drive to both appointments and back home
    mpg = 20  # Her car gets 20 miles per gallon
    gallons_of_gas = total_distance / mpg
    result = gallons_of_gas
    return result

print(solution())