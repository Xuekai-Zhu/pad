def solution():
    """Bill and Jean are both cleaning out their garages. Bill makes a certain number of trips to the dump and Jean makes that many trips plus 6. If they make 40 trips total, how many trips does Jean make?"""
    total_trips = 40
    # Let's call the number of trips Bill makes "x"
    # Then Jean make x + 6 trips
    # So we can write an equation for the total trips: x + (x + 6) = 40
    # Combining like terms gives 2x + 6 = 40
    # Subtracting 6 from both sides gives 2x = 34
    # Dividing by 2 gives x = 17
    # So Bill makes 17 trips and Jean makes 23 trips (17 + 6)
    jeans_trips = 17 + 6
    result = jeans_trips
    return result

print(solution())