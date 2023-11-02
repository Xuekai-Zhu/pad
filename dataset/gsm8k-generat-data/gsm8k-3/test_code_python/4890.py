def solution():
    """Before Marcus went on a road trip to LA, his car had 1728 miles on it. He filled his empty gas tank twice and used up all the gas on the trip. If Marcus's car gets 30 miles per gallon and holds 20 gallons of gas, how many miles does Marcus' car have on it now?"""
    # Define the initial number of miles on Marcus's car
    initial_miles = 1728

    # Define the car's fuel efficiency in miles per gallon
    fuel_efficiency = 30

    # Define the car's gas tank capacity in gallons
    gas_tank_capacity = 20

    # Calculate the total distance Marcus's car can travel on a full tank of gas
    total_distance = fuel_efficiency * gas_tank_capacity

    # Calculate the total distance Marcus's car traveled on the road trip
    road_trip_distance = 2 * total_distance

    # Calculate the current number of miles on Marcus's car
    current_miles = initial_miles + road_trip_distance

    # Display the current number of miles on Marcus's car
    result = current_miles
    return result

print(solution())