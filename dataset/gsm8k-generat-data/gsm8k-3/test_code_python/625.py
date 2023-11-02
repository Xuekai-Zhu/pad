def solution():
    """A town is trying to clear litter from its streets. The council pays for adding 14 trash cans to the streets and also pays for adding twice as many trash cans to the back of stores. How many trash cans has the town paid for?"""
    # Define the number of trash cans added to the streets
    street_cans = 14

    # Calculate the number of trash cans added to the back of stores
    store_cans = 2 * street_cans

    # Calculate the total number of trash cans paid for by the council
    total_cans = street_cans + store_cans

    # Display the total number of trash cans
    result = total_cans
    return result

print(solution())