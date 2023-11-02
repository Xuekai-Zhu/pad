def solution():
    total_guitars = 27

    # Let's assume Steve has x number of guitars
    x = total_guitars / 7  # 7 is the sum of the ratios 2:1:3

    # Barbeck has 2 times as many guitars as Steve
    barbeck_guitars = 2 * x

    # Davey has 3 times as many guitars as Barbeck
    davey_guitars = 3 * barbeck_guitars

    result = davey_guitars
    return result

print(solution())