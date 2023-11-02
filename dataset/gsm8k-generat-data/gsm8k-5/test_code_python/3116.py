def solution():
    # Calculate the number of passengers at each stage of the flight
    passengers_before_texas = 124
    passengers_after_texas = passengers_before_texas - 58 + 24
    passengers_after_nc = passengers_after_texas - 47 + 14

    # Calculate the total number of passengers on the flight
    total_passengers = passengers_after_nc + 10  # Including crew members

    result = total_passengers
    return result

print(solution())