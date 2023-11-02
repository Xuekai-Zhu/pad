def solution():
     total_clients = 30
     vegan_clients = 7
     kosher_clients = 8
     both_vegan_and_kosher_clients = 3
     non_kosher_nor_vegan_clients = total_clients - (vegan_clients + kosher_clients + both_vegan_and_kosher_clients)
     result = non_kosher_nor_vegan_clients
     return result

print(solution())