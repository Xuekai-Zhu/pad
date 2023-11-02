def solution():
    """A car uses 20 gallons of gas to travel 400 miles. Mr. Montero's car has 8 gallons in it. How many more gallons of gas does he need to travel 600 miles, back and forth?"""
    miles_per_gallon = 400 / 20
    needed_gallons = (600 / miles_per_gallon) - 8
    result = needed_gallons * 2 # round trip
    return result

print(solution())