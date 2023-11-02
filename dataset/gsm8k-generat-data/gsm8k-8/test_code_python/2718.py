def solution():
    # Define the weight carried by each type of musician
    trumpet_weight = 5
    clarinet_weight = 5
    trombone_weight = 10
    tuba_weight = 20
    drum_weight = 15

    # Calculate the total weight carried by each type of musician
    total_trumpet_weight = trumpet_weight * 6
    total_clarinet_weight = clarinet_weight * 9
    total_trombone_weight = trombone_weight * 8
    total_tuba_weight = tuba_weight * 3
    total_drum_weight = drum_weight * 2

    # Calculate the total weight carried by the marching band
    total_weight = total_trumpet_weight + total_clarinet_weight + total_trombone_weight + total_tuba_weight + total_drum_weight
    result = total_weight
    return result

print(solution())