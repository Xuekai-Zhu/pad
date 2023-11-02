def solution():
    """Janet has to drive 30 miles east from home to see her dermatologist and 50 miles west from home to see her gynecologist. If she has appointments with both doctors on the same day, how many gallons of gas does she use driving to both appointments and back home again, if her car gets 20 miles per gallon?"""
    total_distance = (30 + 50) * 2 # Round trip
    fuel_efficiency = 20 # miles per gallon
    gallons_used = total_distance / fuel_efficiency
    result = gallons_used
    return result

print(solution())