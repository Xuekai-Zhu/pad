def solution():
    """An airplane was flying from California to Virginia. The flight started with 124 passengers. They made a layover in Texas. 58 passengers got off and 24 got on. From there, they flew to North Carolina, where 47 people got off and 14 got on, before flying to Virginia. There were also a total of 10 crew members on board for the entire flight. How many people landed in Virginia?"""
    initial_passengers = 124
    passengers_off_in_Texas = 58
    passengers_on_in_Texas = 24
    passengers_off_in_NC = 47
    passengers_on_in_NC = 14
    crew_members = 10
    total_passengers = initial_passengers - passengers_off_in_Texas + passengers_on_in_Texas - passengers_off_in_NC + passengers_on_in_NC + crew_members
    result = total_passengers
    return result

print(solution())