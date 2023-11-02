def solution():
    """Carla needs to drive her car to do a bunch of errands. She needs to drive 8 miles to the grocery store, 6 miles to pick up her kids from school, 12 miles to drop her kids off at soccer practice, and twice the distance from the school to soccer practice to get everyone home again. If Carla's car gets 25 miles per gallon, and gas costs $2.50, how much will Carla have to spend on gas for her trip?"""
    # Calculate the total distance Carla will be driving
    total_distance = 8 + 6 + 12 + 2 * 6
    # Calculate the number of gallons of gas needed
    gallons_needed = total_distance / 25
    # Calculate the total cost of gas
    total_cost = gallons_needed * 2.5
    result = total_cost
    return result

print(solution())