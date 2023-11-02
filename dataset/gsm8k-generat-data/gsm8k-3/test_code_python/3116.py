def solution():
    """An airplane was flying from California to Virginia. The flight started with 124 passengers. They made a layover in Texas. 58 passengers got off and 24 got on. From there, they flew to North Carolina, where 47 people got off and 14 got on, before flying to Virginia. There were also a total of 10 crew members on board for the entire flight. How many people landed in Virginia?"""
    # Define the initial number of passengers
    initial_passengers = 124

    # Calculate the number of passengers after the first layover in Texas
    passengers_texas = initial_passengers - 58 + 24

    # Calculate the number of passengers after the second layover in North Carolina
    passengers_nc = passengers_texas - 47 + 14

    # Calculate the total number of passengers, including crew members
    total_passengers = passengers_nc + 10

    # Display the total number of passengers who landed in Virginia
    result = total_passengers
    return result

print(solution())