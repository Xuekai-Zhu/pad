def solution():
    """In a yard, the number of tanks is five times the number of trucks. If there are 20 trucks in the yard, calculate the total number of tanks and trucks in the yard."""
    # Define the number of trucks in the yard
    trucks = 20

    # Calculate the number of tanks in the yard
    tanks = 5 * trucks

    # Calculate the total number of vehicles in the yard
    total_vehicles = trucks + tanks

    # return the result
    result = (trucks, tanks, total_vehicles)
    return result

print(solution())