def solution():
    """Janet has to drive 30 miles east from home to see her dermatologist and 50 miles west from home to see her gynecologist. If she has appointments with both doctors on the same day, how many gallons of gas does she use driving to both appointments and back home again, if her car gets 20 miles per gallon?"""
    total_distance = 30 + 50 + 30 + 50  # roundtrip to both doctors and back home
    miles_per_gallon = 20
    gallons_needed = total_distance / miles_per_gallon
    result = gallons_needed
    return result

print(solution())