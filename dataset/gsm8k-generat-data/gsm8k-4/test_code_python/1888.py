def solution():
    """The New York City Council bought 200 streetlights to modernize its squares. But they don't have enough squares to use all the streetlights bought. Knowing that there are 15 squares in New York and that each park will have 12 new streetlights bought by the city council, how many unused streetlights will remain?"""
    # Define the total number of streetlights and the number of streetlights per square
    total_streetlights = 200
    streetlights_per_square = 12

    # Calculate the maximum number of streetlights that can be used in all the squares
    max_streetlights = streetlights_per_square * 15

    # Calculate the number of unused streetlights
    unused_streetlights = total_streetlights - max_streetlights

    # return the result
    result = unused_streetlights
    return result

print(solution())