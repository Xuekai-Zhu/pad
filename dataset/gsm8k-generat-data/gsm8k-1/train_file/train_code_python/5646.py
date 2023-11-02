def solution():
    """Carol fills up her gas tank as she is driving home for college, which is 220 miles away. She can get 20 miles to the gallon in her car, which has a 16-gallon gas tank. How many more miles will she be able to drive after she gets home and without filling her tank again?"""
    miles_to_college = 220
    miles_per_gallon = 20
    tank_size = 16
    gallons_used = miles_to_college / miles_per_gallon
    remaining_gallons = tank_size - gallons_used
    remaining_miles = remaining_gallons * miles_per_gallon
    result = remaining_miles
    return result

print(solution())