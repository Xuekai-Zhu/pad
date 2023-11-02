def solution():
    """A school is getting ready to open for the year and the sports class is organizing the equipment they have been donated. In total, they have 300 donations to organize. 60 of these were basketball hoops, half of which also had basketballs included as part of the donation. 120 pool floats were donated, but a quarter of these were damaged and were discarded before the sports class arrived. There were 50 footballs, 40 tennis balls, and the remaining donations were basketballs. In total, how many basketballs have been donated?"""
    # Define the number of basketball hoops
    basketball_hoops = 60

    # Calculate the number of basketballs included in the basketball hoop donations
    basketballs_basketball_hoops = basketball_hoops * 0.5

    # Calculate the number of pool floats after discarding the damaged ones
    pool_floats = 120 * 0.75

    # Calculate the total number of donations that were not basketballs
    non_basketballs = basketball_hoops + pool_floats + 50 + 40

    # Calculate the number of basketballs
    basketballs = 300 - non_basketballs + basketballs_basketball_hoops

    # return the result
    result = basketballs
    return result

print(solution())