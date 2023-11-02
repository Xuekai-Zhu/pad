def solution():
    miles_to_dermatologist = 30
    miles_to_gynecologist = 50
    total_miles = miles_to_dermatologist + miles_to_gynecologist

    miles_per_gallon = 20

    # Calculate the total gallons of gas used
    total_gallons = total_miles / miles_per_gallon

    # Round up to the nearest gallon
    total_gallons = math.ceil(total_gallons)

    result = total_gallons
    return result

print(solution())