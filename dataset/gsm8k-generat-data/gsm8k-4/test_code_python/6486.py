def solution():
    """Janet has to drive 30 miles east from home to see her dermatologist and 50 miles west from home to see her gynecologist. If she has appointments with both doctors on the same day, how many gallons of gas does she use driving to both appointments and back home again, if her car gets 20 miles per gallon?"""
    # Define the distance to each doctor's office
    dermatologist_distance = 30
    gynecologist_distance = 50

    # Calculate the total distance Janet needs to drive
    total_distance = dermatologist_distance + gynecologist_distance

    # Calculate the number of gallons of gas needed based on her car's fuel efficiency
    gas_used = total_distance / 20

    # Round the result to the nearest tenth
    result = round(gas_used, 1)
    return result

print(solution())