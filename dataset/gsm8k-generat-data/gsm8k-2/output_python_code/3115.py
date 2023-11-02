def solution():
    """An airplane was flying from California to Virginia. The flight started with 124 passengers. They made a layover in Texas. 58 passengers got off and 24 got on. From there, they flew to North Carolina, where 47 people got off and 14 got on, before flying to Virginia. There were also a total of 10 crew members on board for the entire flight. How many people landed in Virginia?"""
    initial_passengers = 124
    texas_off = 58
    texas_on = 24
    nc_off = 47
    nc_on = 14
    crew_members = 10
    total_passengers = initial_passengers - texas_off + texas_on - nc_off + nc_on + crew_members
    result = total_passengers
    return result

print(solution())