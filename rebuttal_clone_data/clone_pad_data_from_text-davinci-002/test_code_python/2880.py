def solution():
    total_fingers = 210
    clients = 200 / 20
    non_clients = total_fingers - (clients * 10)
    result = non_clients
    
    return result

print(solution())