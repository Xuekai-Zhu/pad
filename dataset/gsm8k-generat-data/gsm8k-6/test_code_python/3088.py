def solution():
    # Calculate the number of refills needed for a one-way trip
    one_way_refills = 280 / 40  # Keanu's motorcycle consumes 8 liters of gasoline per 40 miles
    # Calculate the number of refills needed for a round trip
    round_trip_refills = one_way_refills * 2
    result = round_trip_refills
    return result

print(solution())