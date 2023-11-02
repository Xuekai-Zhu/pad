def solution():
    """Megan is delivering meals on wheels. Out of her 30 clients, 7 need vegan meals, 8 need kosher meals, and three people need meals that are both vegan and kosher. How many meals does Megan deliver that are neither kosher nor vegan?"""
    total_clients = 30
    vegan_clients = 7
    kosher_clients = 8
    both_clients = 3
    neither = total_clients - (vegan_clients + kosher_clients - both_clients)
    result = neither
    return result

print(solution())