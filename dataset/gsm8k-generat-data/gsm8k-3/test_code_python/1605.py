def solution():
    """There are 92 students altogether. Twenty of them ride the school bus home together, 5/8 of the remaining ride their own bike home, and the rest whose houses are near the school walk home. How many students are walking home?"""
    # Define the total number of students
    TOTAL_STUDENTS = 92

    # Calculate the number of students who ride the bus
    bus_riders = 20

    # Calculate the number of students who don't ride the bus
    non_bus_riders = TOTAL_STUDENTS - bus_riders

    # Calculate the number of students who ride their own bikes
    bike_riders = int((5/8) * non_bus_riders)

    # Calculate the number of students who walk
    walkers = non_bus_riders - bike_riders

    # Display the number of students who walk home
    result = walkers
    return result

print(solution())