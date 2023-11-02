def solution():
    # Let's say Steve has x number of guitars
    x = 1

    # Barbeck has two times as many guitars as Steve
    barbeck = 2 * x

    # Davey has three times as many guitars as Barbeck
    davey = 3 * barbeck

    # The total number of guitars is 27
    total = x + barbeck + davey

    # Solve for davey
    davey_guitars = (27 - x - barbeck) / 3

    result = davey_guitars
    return result

print(solution())