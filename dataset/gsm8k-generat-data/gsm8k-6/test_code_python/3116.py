def solution():
    # Calculate the total number of passengers on the plane at the end of the flight
    passengers_start = 124  # initial number of passengers
    passengers_layover = passengers_start - 58 + 24  # number of passengers after layover in Texas
    passengers_end = passengers_layover - 47 + 14  # number of passengers after getting off in North Carolina and getting on in North Carolina
    total_passengers = passengers_end + 10  # add the crew members
    result = total_passengers
    return result

print(solution())