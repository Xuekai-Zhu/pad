def solution():
    """Timmy, Tommy and Tina are filling up a kiddie pool in their backyard. Each has a pail they fill with water from a house before dumping it into the pool. If Timmy's pail holds twice as much water as Tommy's, and Tommy's holds 2 gallons more than Tina's, and Tina's is 4 gallons, how much water do the three of them fill the pool with after 3 trips each?"""
    # Define the volume of Tina's pail
    tina_pail = 4

    # Define the volume of Tommy's pail
    tommy_pail = tina_pail + 2

    # Define the volume of Timmy's pail
    timmy_pail = tommy_pail * 2

    # Calculate the total volume of water that can be carried in one trip
    total_trip_volume = tina_pail + tommy_pail + timmy_pail

    # Calculate the total volume of water that can be carried in three trips by all three
    total_volume = total_trip_volume * 3

    # Return the result
    result = total_volume
    return result

print(solution())