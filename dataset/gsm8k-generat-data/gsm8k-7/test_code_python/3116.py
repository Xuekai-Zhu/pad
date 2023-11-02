def solution():
    initial_passengers = 124
    passengers_off_in_texas = 58
    passengers_on_in_texas = 24
    passengers_off_in_NC = 47
    passengers_on_in_NC = 14
    crew_members = 10

    # Calculate the number of passengers and crew members after the layover in Texas
    passengers_in_texas = initial_passengers - passengers_off_in_texas + passengers_on_in_texas + crew_members

    # Calculate the number of passengers and crew members after the flight to North Carolina
    passengers_in_NC = passengers_in_texas - passengers_off_in_NC + passengers_on_in_NC + crew_members

    # Calculate the number of passengers and crew members that landed in Virginia
    passengers_in_Virginia = passengers_in_NC + crew_members
    result = passengers_in_Virginia
    return result

print(solution())