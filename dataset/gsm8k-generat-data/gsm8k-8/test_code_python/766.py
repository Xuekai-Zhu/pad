def solution():
    total_clients = 30
    vegan_clients = 7
    kosher_clients = 8
    vegan_and_kosher_clients = 3

    # calculate the number of meals that are either vegan or kosher (or both)
    vegan_or_kosher_clients = vegan_clients + kosher_clients - vegan_and_kosher_clients

    # calculate the number of clients that are neither vegan nor kosher
    neither_vegan_nor_kosher_clients = total_clients - vegan_or_kosher_clients

    # calculate the number of meals that are neither vegan nor kosher
    neither_vegan_nor_kosher_meals = neither_vegan_nor_kosher_clients

    result = neither_vegan_nor_kosher_meals
    return result

print(solution())