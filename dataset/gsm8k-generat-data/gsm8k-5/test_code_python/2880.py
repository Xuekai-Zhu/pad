def solution():
    # Calculate the number of clients in the salon
    num_clients = 200 / 20  # Each client pays $20 for a manicure

    # Calculate the total number of fingers in the salon
    total_fingers = 210

    # Calculate the number of fingers belonging to the clients
    fingers_of_clients = num_clients * 10

    # Calculate the number of fingers not belonging to clients
    fingers_not_clients = total_fingers - fingers_of_clients
    num_not_clients = fingers_not_clients / 10
    result = num_not_clients
    return result

print(solution())