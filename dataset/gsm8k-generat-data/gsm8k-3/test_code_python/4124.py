def solution():
    """Timmy, Tommy and Tina are filling up a kiddie pool in their backyard.  Each has a pail they fill with water from a house before dumping it into the pool.  If Timmy's pail holds twice as much water as Tommy's, and Tommy's holds 2 gallons more than Tina's, and Tina's is 4 gallons, how much water do the three of them fill the pool with after 3 trips each?"""
    # Define the amount of water each pail can hold
    tina_pail = 4
    tommy_pail = tina_pail + 2
    timmy_pail = tommy_pail * 2

    # Calculate the total amount of water each person can carry in one trip
    tina_trips = tina_pail * 3
    tommy_trips = tommy_pail * 3
    timmy_trips = timmy_pail * 3

    # Calculate the total amount of water the three of them can carry in one trip
    total_trips = tina_trips + tommy_trips + timmy_trips

    # Display the total amount of water they can fill the pool with after 3 trips each
    result = total_trips * 3
    return result

print(solution())