def solution():
    total_clients = 30
    vegan_clients = 7
    kosher_clients = 8
    vegan_and_kosher_clients = 3

    # Calculate the number of clients who need either vegan or kosher meals
    total_vegan_or_kosher_clients = vegan_clients + kosher_clients - vegan_and_kosher_clients

    # Calculate the number of clients who need neither vegan nor kosher meals
    neither_vegan_nor_kosher_clients = total_clients - total_vegan_or_kosher_clients

    # Calculate the total number of meals that Megan delivers that are neither kosher nor vegan
    meals_delivered = neither_vegan_nor_kosher_clients

    result = meals_delivered
    return result

print(solution())