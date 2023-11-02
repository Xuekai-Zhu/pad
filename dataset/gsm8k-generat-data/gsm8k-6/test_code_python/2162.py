def solution():
    # Calculate the gallons of gas used for highway driving
    gallons_highway = 210 / 35  # their car gets 35 miles for each gallon of gas
    # Calculate the gallons of gas used for city driving
    gallons_city = 54 / 18  # their car gets 18 miles for each gallon of gas
    # Calculate the total gallons of gas used
    total_gallons = gallons_highway + gallons_city
    result = total_gallons
    return result

print(solution())