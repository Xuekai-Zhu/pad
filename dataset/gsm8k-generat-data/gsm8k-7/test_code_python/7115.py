def solution():
    trip_frequency = 0.4
    drop_frequency_given_trip = 0.25

    # Calculate the frequency of dropping coffee
    drop_frequency = trip_frequency * drop_frequency_given_trip

    # Calculate the frequency of not dropping coffee
    not_drop_frequency = 1 - drop_frequency

    # Convert the frequency to a percentage
    not_drop_percent = not_drop_frequency * 100
    result = not_drop_percent
    return result

print(solution())