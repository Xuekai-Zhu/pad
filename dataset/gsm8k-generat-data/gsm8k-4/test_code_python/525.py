def solution():
    """Carla needs to drive her car to do a bunch of errands. She needs to drive 8 miles to the grocery store, 6 miles to pick up her kids from school, 12 miles to drop her kids off at soccer practice, and twice the distance from the school to soccer practice to get everyone home again. If Carla's car gets 25 miles per gallon, and gas costs $2.50, how much will Carla have to spend on gas for her trip?"""
    
    # Define the distances that Carla needs to travel
    grocery_distance = 8
    school_distance = 6
    soccer_distance = 12
    home_distance = 2 * school_distance

    # Calculate the total distance Carla needs to travel
    total_distance = grocery_distance + school_distance + soccer_distance + home_distance

    # Calculate the amount of gas Carla will need in gallons
    gas_needed = total_distance / 25

    # Calculate the total cost of gas
    gas_cost = gas_needed * 2.50

    result = gas_cost
    return result

print(solution())