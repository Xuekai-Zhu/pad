def solution():
    """A nail salon was completely booked at 2 pm for manicures. Each manicure costs $20.00 per client so the salon made $200.00. If there are 210 fingers in the salon at 2 pm, and everyone has 10 fingers, how many people in the salon are not clients?"""
    total_clients = 10
    total_fingers = 210
    num_clients = total_fingers / total_clients
    clients_paid = num_clients * 20
    total_paid = 200
    num_non_clients = (total_paid - clients_paid) / 20
    result = num_non_clients
    return result

print(solution())