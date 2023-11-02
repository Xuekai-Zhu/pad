def solution():
    # Calculate the number of clients at the salon
    num_clients = 200/20

    # Calculate the total number of fingers being serviced
    num_fingers = num_clients * 10

    # Calculate the number of people not receiving a manicure
    num_non_clients = (210 - num_fingers) / 10
    result = num_non_clients
    return result

print(solution())