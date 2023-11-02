def solution():
    
    total_clients = 30
    vegan_clients = 7
    kosher_clients = 8
    vegan_and_kosher = 3
    non_vegan_non_kosher = total_clients - (vegan_clients + kosher_clients - vegan_and_kosher)
    result = non_vegan_non_kosher
    return result

print(solution())