def solution():
    """There are one-third as many Ford trucks as Dodge trucks in the parking lot of the Taco Castle.  But there are twice as many Ford trucks as Toyota trucks in this parking lot, and there are half as many Volkswagen Bugs as there are Toyota trucks in this same parking lot.  If there are 5 Volkswagen Bugs in the parking lot, how many Dodge trucks are in the parking lot of the Taco Castle?"""
    # Define the number of Volkswagen Bugs in the parking lot
    BUGS = 5

    # Calculate the number of Toyota trucks in the parking lot
    toyota_trucks = BUGS * 2

    # Calculate the number of Ford trucks in the parking lot
    ford_trucks = toyota_trucks * 2

    # Calculate the number of Dodge trucks in the parking lot
    dodge_trucks = 3 * ford_trucks

    # Display the number of Dodge trucks
    result = dodge_trucks
    return result

print(solution())