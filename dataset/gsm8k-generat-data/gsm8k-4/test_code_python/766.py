def solution():
    """Megan is delivering meals on wheels. Out of her 30 clients, 7 need vegan meals, 8 need kosher meals, and three people need meals that are both vegan and kosher. How many meals does Megan deliver that are neither kosher nor vegan?"""
    # Define the total number of clients and the number of clients who need vegan or kosher meals
    total_clients = 30
    vegan_clients = 7
    kosher_clients = 8

    # Calculate the number of clients who need both vegan and kosher meals
    vegan_kosher_clients = 3

    # Calculate the number of clients who need only vegan meals
    only_vegan_clients = vegan_clients - vegan_kosher_clients

    # Calculate the number of clients who need only kosher meals
    only_kosher_clients = kosher_clients - vegan_kosher_clients

    # Calculate the number of clients who don't need either vegan or kosher meals
    neither_vegan_nor_kosher_clients = total_clients - (only_vegan_clients + only_kosher_clients + vegan_kosher_clients)

    # return the result
    result = neither_vegan_nor_kosher_clients
    return result

print(solution())