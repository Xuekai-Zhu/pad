def solution():
    total_clients = 30
    vegan_clients = 7
    kosher_clients = 8
    both_vegan_kosher_clients = 3

    # Calculate the number of clients who are not vegan or kosher
    neither_vegan_kosher_clients = total_clients - (vegan_clients + kosher_clients - both_vegan_kosher_clients)

    # Calculate the total number of meals that Megan delivers that are neither vegan nor kosher
    neither_vegan_kosher_meals = neither_vegan_kosher_clients

    result = neither_vegan_kosher_meals
    return result

print(solution())