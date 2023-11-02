def solution():
    """In a yard, the number of tanks is five times the number of trucks. If there are 20 trucks in the yard, calculate the total number of tanks and trucks in the yard."""
    # Define the ratio of tanks to trucks
    TANK_TRUCK_RATIO = 5/1

    # Get the number of trucks in the yard
    trucks_in_yard = 20

    # Calculate the number of tanks in the yard
    tanks_in_yard = TANK_TRUCK_RATIO * trucks_in_yard

    # Calculate the total number of tanks and trucks in the yard
    total = trucks_in_yard + tanks_in_yard

    # Display the total number of tanks and trucks in the yard
    result = total
    return result

print(solution())