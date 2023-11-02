def solution():
    total_berrie = 1100

    # Let's assume Skylar has x berries
    x = total_berrie / 7

    # Steve has twice the number of berries as Skylar, i.e., 2*x berries
    # Stacy has four times as many berries as Steve, i.e., 4*(2*x) berries, which simplifies to 8*x berries
    stacy_berrie = 8*x
    result = stacy_berrie
    return result

print(solution())