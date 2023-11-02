def solution():
    """Carla needs to drive her car to do a bunch of errands. She needs to drive 8 miles to the grocery store, 6 miles to pick up her kids from school, 12 miles to drop her kids off at soccer practice, and twice the distance from the school to soccer practice to get everyone home again. If Carla's car gets 25 miles per gallon, and gas costs $2.50, how much will Carla have to spend on gas for her trip?"""
    grocery_store_distance = 8
    school_distance = 6
    soccer_practice_distance = 12
    round_trip_distance = 2 * (soccer_practice_distance - school_distance)
    total_distance = grocery_store_distance + school_distance + soccer_practice_distance + round_trip_distance
    miles_per_gallon = 25
    gas_price = 2.50
    gallons_needed = total_distance / miles_per_gallon
    total_cost = gallons_needed * gas_price
    result = total_cost
    
    return result

print(solution())