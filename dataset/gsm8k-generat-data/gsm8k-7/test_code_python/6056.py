def solution():
    start_time = 8 * 60  # convert start time to minutes
    paul_arrival = start_time + 25
    amoura_arrival = paul_arrival + 30
    ingrid_arrival = amoura_arrival + 3 * 30  # three times later than Amoura

    # Calculate the total minutes Ingrid was late to the party
    late_time = ingrid_arrival - start_time
    result = late_time
    return result

print(solution())