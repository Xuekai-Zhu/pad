def solution():
    """At the park, Naomi saw people riding 7 regular bikes and 11 children’s bikes.  Regular bikes have 2 wheels and kid’s bikes have 4 wheels.  How many wheels did Naomi see at the park?"""
    # Define the number of wheels on each type of bike
    REGULAR_BIKE_WHEELS = 2
    CHILD_BIKE_WHEELS = 4

    # Define the number of each type of bike Naomi saw
    regular_bikes = 7
    child_bikes = 11

    # Calculate the total number of wheels Naomi saw
    total_wheels = regular_bikes * REGULAR_BIKE_WHEELS + child_bikes * CHILD_BIKE_WHEELS

    # Display the total number of wheels
    result = total_wheels
    return result

print(solution())