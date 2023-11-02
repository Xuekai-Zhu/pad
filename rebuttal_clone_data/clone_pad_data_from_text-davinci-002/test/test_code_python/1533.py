def solution():
    trumpet_weight = 5
    clarinet_weight = 5
    trombone_weight = 10
    tuba_weight = 20
    drum_weight = 15
    trumpet_count = 6
    clarinet_count = 9
    trombone_count = 8
    tuba_count = 3
    drum_count = 2
    total_weight = (trumpet_count * trumpet_weight) + (clarinet_count * clarinet_weight) + (trombone_count * trombone_weight) + (tuba_count * tuba_weight) + (drum_count * drum_weight)
    result = total_weight
    return result

print(solution())