def solution():
    
    total_clients = 30
    vegan_clients = 7
    kosher_clients = 8
    both_clients = 3
    neither = total_clients - (vegan_clients + kosher_clients - both_clients)
    result = neither
    return result

print(solution())