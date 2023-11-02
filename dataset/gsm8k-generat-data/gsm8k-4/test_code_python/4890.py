def solution():
    """Before Marcus went on a road trip to LA, his car had 1728 miles on it. He filled his empty gas tank twice and used up all the gas on the trip. If Marcus's car gets 30 miles per gallon and holds 20 gallons of gas, how many miles does Marcus' car have on it now?"""
    # Define the initial number of miles and the fuel capacity
    initial_miles = 1728
    fuel_capacity = 20

    # Calculate the total distance Marcus could drive on a full tank of gas
    miles_per_tank = 30 * fuel_capacity

    # Calculate the number of miles driven on the trip
    miles_driven = miles_per_tank * 2

    # Calculate the current number of miles on the car
    current_miles = initial_miles + miles_driven

    # Return the result
    result = current_miles
    return result

print(solution())