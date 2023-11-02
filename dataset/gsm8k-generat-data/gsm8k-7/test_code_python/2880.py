def solution():
    total_clients = 200 / 20  # $200 was made, and each manicure is $20
    total_fingers = 210
    fingers_per_client = 10

    # Calculate the total number of clients
    num_clients = total_fingers / fingers_per_client

    # Calculate the number of people in the salon who are not clients
    num_non_clients = num_clients - total_clients
    result = num_non_clients
    return result

print(solution())