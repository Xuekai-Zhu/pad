def solution():
    """Tony has to run several errands in a day.  He needs to drive 10 miles to get groceries, 15 miles to get a haircut and 5 miles to go to a doctor's appointment.  How many miles will Tony have driven when he is halfway through driving around for his errands?"""
    # Define the distances to each errand
    grocery_distance = 10
    haircut_distance = 15
    doctor_distance = 5

    # Calculate the total distance Tony needs to drive
    total_distance = grocery_distance + haircut_distance + doctor_distance

    # Calculate the halfway point of the total distance
    halfway_distance = total_distance/2

    # Initialize a variable to keep track of the distance driven so far
    distance_driven = 0

    # Determine how far Tony needs to drive to reach the halfway point
    if halfway_distance <= grocery_distance:
        distance_driven = halfway_distance
    elif halfway_distance <= grocery_distance + haircut_distance:
        distance_driven = grocery_distance + (halfway_distance - grocery_distance)/2
    else:
        distance_driven = total_distance - (halfway_distance - doctor_distance)

    # Display the distance Tony has driven when he is halfway done with his errands
    result = distance_driven
    return result

print(solution())