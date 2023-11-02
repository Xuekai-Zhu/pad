def solution():
    # Calculate the arrival time of Amoura
    paul_arrival = 25  # Paul arrived at 8:25
    amoura_arrival = paul_arrival + 30  # Amoura arrived 30 minutes after Paul

    # Calculate the arrival time of Ingrid
    ingrid_delay = 3 * 30  # Ingrid was three times later than Amoura
    ingrid_arrival = amoura_arrival + ingrid_delay  # Add Ingrid's delay to Amoura's arrival time

    # Calculate the total delay of Ingrid
    total_delay = ingrid_arrival - 480  # 480 is the time the party was supposed to start (8:00 a.m.)
    result = total_delay
    return result

print(solution())