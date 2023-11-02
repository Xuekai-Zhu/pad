def solution():
    """Megan is delivering meals on wheels. Out of her 30 clients, 7 need vegan meals, 8 need kosher meals, and three people need meals that are both vegan and kosher. How many meals does Megan deliver that are neither kosher nor vegan?"""
    total_clients = 30
    vegan_clients = 7
    kosher_clients = 8
    vegan_and_kosher = 3
    non_vegan_non_kosher = total_clients - (vegan_clients + kosher_clients - vegan_and_kosher)
    result = non_vegan_non_kosher
    return result

print(solution())