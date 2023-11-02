def solution():
    trumpet_weight = 5
    clarinet_weight = 5
    trombone_weight = 10
    tuba_weight = 20
    drum_weight = 15
    num_trumpets = 6
    num_clarinets = 9
    num_trombones = 8
    num_tubas = 3
    num_drummers = 2

    # Calculate the total weight carried by the trumpet players
    total_trumpet_weight = num_trumpets * trumpet_weight

    # Calculate the total weight carried by the clarinet players
    total_clarinet_weight = num_clarinets * clarinet_weight

    # Calculate the total weight carried by the trombone players
    total_trombone_weight = num_trombones * trombone_weight

    # Calculate the total weight carried by the tuba players
    total_tuba_weight = num_tubas * tuba_weight

    # Calculate the total weight carried by the drum players
    total_drum_weight = num_drummers * drum_weight

    # Calculate the total weight carried by the marching band
    total_weight = (total_trumpet_weight + total_clarinet_weight + total_trombone_weight + total_tuba_weight
                    + total_drum_weight)
    result = total_weight
    return result

print(solution())