def solution():
    # Calculate the total number of clients in the salon
    num_clients = 200 / 20  # each client pays $20.00 per manicure

    # Calculate the total number of people in the salon
    total_people = 210 / 10  # everyone has 10 fingers

    # Calculate the number of people who are not clients
    num_not_clients = total_people - num_clients

    result = num_not_clients
    return result

print(solution())