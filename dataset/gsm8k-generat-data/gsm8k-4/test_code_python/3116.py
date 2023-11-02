def solution():
    """An airplane was flying from California to Virginia. The flight started with 124 passengers. They made a layover in Texas. 58 passengers got off and 24 got on. From there, they flew to North Carolina, where 47 people got off and 14 got on, before flying to Virginia. There were also a total of 10 crew members on board for the entire flight. How many people landed in Virginia?"""
    # Define the initial number of passengers
    passengers = 124

    # Subtract the number of passengers who got off and add the number of passengers who got on at each stop
    passengers -= 58
    passengers += 24
    passengers -= 47
    passengers += 14

    # Add the number of crew members who were on board for the entire flight
    passengers += 10

    # Display the final number of passengers who landed in Virginia
    result = passengers
    return result

print(solution())