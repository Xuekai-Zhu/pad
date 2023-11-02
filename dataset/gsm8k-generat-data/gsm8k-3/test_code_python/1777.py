def solution():
    """A school is getting ready to open for the year and the sports class is organizing the equipment they have been donated. In total, they have 300 donations to organize. 60 of these were basketball hoops, half of which also had basketballs included as part of the donation. 120 pool floats were donated, but a quarter of these were damaged and were discarded before the sports class arrived. There were 50 footballs, 40 tennis balls, and the remaining donations were basketballs. In total, how many basketballs have been donated?"""
    # Calculate the number of basketballs included in the basketball hoop donations
    basketball_hoops = 60
    basketballs_in_hoops = basketball_hoops / 2

    # Calculate the number of undamaged pool floats
    pool_floats = 120
    undamaged_floats = pool_floats * 0.75

    # Calculate the total number of basketballs
    total_basketballs = basketballs_in_hoops + undamaged_floats + 50 + 40

    # Calculate the remaining number of donations that were basketballs
    remaining_donations = 300 - basketball_hoops - pool_floats - 50 - 40

    # Add the remaining basketball donations to the total
    total_basketballs += remaining_donations

    # Display the total number of basketballs donated
    result = total_basketballs
    return result

print(solution())