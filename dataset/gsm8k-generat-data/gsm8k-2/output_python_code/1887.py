def solution():
    """The New York City Council bought 200 streetlights to modernize its squares. But they don't have enough squares to use all the streetlights bought. Knowing that there are 15 squares in New York and that each park will have 12 new streetlights bought by the city council, how many unused streetlights will remain?"""
    total_streetlights = 200
    total_squares = 15
    streetlights_per_square = 12
    used_streetlights = streetlights_per_square * total_squares
    unused_streetlights = total_streetlights - used_streetlights
    result = unused_streetlights
    return result

print(solution())