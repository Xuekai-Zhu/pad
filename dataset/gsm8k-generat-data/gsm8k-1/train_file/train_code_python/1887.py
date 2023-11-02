def solution():
    """The New York City Council bought 200 streetlights to modernize its squares. But they don't have enough squares to use all the streetlights bought. Knowing that there are 15 squares in New York and that each park will have 12 new streetlights bought by the city council, how many unused streetlights will remain?"""
    total_streetlights = 200
    parks_with_new_lights = 15
    streetlights_per_park = 12
    streetlights_used = parks_with_new_lights * streetlights_per_park
    streetlights_unused = total_streetlights - streetlights_used
    result = streetlights_unused
    return result

print(solution())