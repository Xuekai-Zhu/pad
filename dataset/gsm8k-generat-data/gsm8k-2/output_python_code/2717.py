def solution():
    """In the Oprah Winfrey High School marching band, each trumpet and clarinet player carries 5 pounds of weight, each trombone player carries 10 pounds of weight, each tuba player carries 20 pounds of weight, and each drum player carries 15 pounds of weight. If there are 6 trumpets, 9 clarinets, 8 trombones, 3 tubas, and 2 drummers, how much weight does the total marching band carry?"""
    trumpet_weight = 5
    clarinet_weight = 5
    trombone_weight = 10
    tuba_weight = 20
    drum_weight = 15
    total_weight = (6 * trumpet_weight) + (9 * clarinet_weight) + (8 * trombone_weight) + (3 * tuba_weight) + (2 * drum_weight)
    result = total_weight
    return result

print(solution())