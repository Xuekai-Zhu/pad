def solution():
    """A nail salon was completely booked at 2 pm for manicures.  Each manicure costs $20.00 per client so the salon made $200.00.  If there are 210 fingers in the salon at 2 pm, and everyone has 10 fingers, how many people in the salon are not clients?"""
    # Calculate the number of clients at the nail salon
    num_clients = 200 / 20

    # Calculate the number of fingers belonging to clients
    client_fingers = num_clients * 10

    # Calculate the number of non-client fingers
    non_client_fingers = 210 - client_fingers

    # Calculate the number of people who are not clients
    num_non_clients = non_client_fingers / 10

    # Display the number of people who are not clients
    result = num_non_clients
    return result

print(solution())