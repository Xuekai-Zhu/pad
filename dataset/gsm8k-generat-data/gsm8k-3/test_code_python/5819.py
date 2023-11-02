def solution():
    """Casey is pumping water out of her well. She can pump 3 gallons a minute. She has 4 rows of 15 corn plants each, and each plant needs half a gallon of water. She also has 10 pigs, which each need 4 gallons of water, and 20 ducks that each need a quarter of a gallon of water. How many minutes does Casey need to spend pumping water?"""
    # Calculate the total amount of water needed for the corn plants
    corn_water = 0.5 * 15 * 4

    # Calculate the total amount of water needed for the pigs
    pig_water = 4 * 10

    # Calculate the total amount of water needed for the ducks
    duck_water = 0.25 * 20

    # Calculate the total amount of water needed
    total_water = corn_water + pig_water + duck_water

    # Calculate the time required to pump all the water
    pumping_time = total_water / 3

    # Display the pumping time in minutes
    result = pumping_time
    return result

print(solution())