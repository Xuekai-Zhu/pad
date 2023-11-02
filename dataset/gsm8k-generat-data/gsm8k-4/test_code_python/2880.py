def solution():
    """A nail salon was completely booked at 2 pm for manicures. Each manicure costs $20.00 per client so the salon made $200.00. If there are 210 fingers in the salon at 2 pm, and everyone has 10 fingers, how many people in the salon are not clients?"""
    # Define the total number of fingers in the salon
    total_fingers = 210

    # Calculate the number of clients
    num_clients = 200 / 20

    # Calculate the total number of people in the salon
    total_people = total_fingers / 10

    # Calculate the number of non-clients
    num_non_clients = total_people - num_clients

    # Return the result
    result = num_non_clients
    return result

print(solution())