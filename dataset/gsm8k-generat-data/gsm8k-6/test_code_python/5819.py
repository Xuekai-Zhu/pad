def solution():
    # Calculate the total water needed for corn plants
    corn_water = 0.5 * 4 * 15  # each plant needs half a gallon of water, there are 4 rows of 15 plants

    # Calculate the total water needed for pigs
    pig_water = 4 * 10  # each pig needs 4 gallons of water, there are 10 pigs

    # Calculate the total water needed for ducks
    duck_water = 0.25 * 20  # each duck needs a quarter of a gallon of water, there are 20 ducks

    # Calculate the total water needed
    total_water = corn_water + pig_water + duck_water

    # Calculate the time needed to pump the water
    time_needed = total_water / 3  # Casey can pump 3 gallons a minute

    result = time_needed
    return result

print(solution())