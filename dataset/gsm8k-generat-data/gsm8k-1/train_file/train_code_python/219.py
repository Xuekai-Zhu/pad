def solution():
    """A car uses 20 gallons of gas to travel 400 miles. Mr. Montero's car has 8 gallons in it. How many more gallons of gas does he need to travel 600 miles, back and forth?"""
    miles_per_gallon = 400 / 20
    total_miles = 600 * 2
    gallons_needed = (total_miles / miles_per_gallon) - 8
    result = gallons_needed
    return result

print(solution())