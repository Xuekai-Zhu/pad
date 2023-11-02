def solution():
    """The New York City Council bought 200 streetlights to modernize its squares. But they don't have enough squares to use all the streetlights bought. Knowing that there are 15 squares in New York and that each park will have 12 new streetlights bought by the city council, how many unused streetlights will remain?"""
    # Define the number of streetlights per park
    STREETLIGHTS_PER_PARK = 12

    # Define the total number of streetlights bought by the city
    total_streetlights = 200

    # Calculate the number of streetlights needed for all the parks
    streetlights_for_parks = STREETLIGHTS_PER_PARK * 15

    # Calculate the number of unused streetlights
    unused_streetlights = total_streetlights - streetlights_for_parks

    # Display the number of unused streetlights
    result = unused_streetlights
    return result

print(solution())