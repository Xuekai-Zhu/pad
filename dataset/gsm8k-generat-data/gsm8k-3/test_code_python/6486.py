def solution():
    """Janet has to drive 30 miles east from home to see her dermatologist and 50 miles west from home to see her gynecologist. If she has appointments with both doctors on the same day, how many gallons of gas does she use driving to both appointments and back home again, if her car gets 20 miles per gallon?"""
    # Determine the total distance Janet has to travel
    total_distance = 30 + 50 + 30 +50 # East to dermatologist + West to gynecologist + West back home + East back home

    # Determine how many gallons of gas Janet will need for the trip
    gallons_of_gas = total_distance / 20 # Assumes 20 miles per gallon

    # Display the number of gallons of gas needed
    result = gallons_of_gas
    return result

print(solution())