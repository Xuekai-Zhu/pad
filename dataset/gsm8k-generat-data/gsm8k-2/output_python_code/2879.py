def solution():
    """A nail salon was completely booked at 2 pm for manicures. Each manicure costs $20.00 per client so the salon made $200.00. If there are 210 fingers in the salon at 2 pm, and everyone has 10 fingers, how many people in the salon are not clients?"""
    total_clients = 10  # Each client has 10 fingers
    total_fingers = 210
    total_clients_fingers = total_clients * 20  # 20 fingers per client
    total_clients_num = total_clients_fingers // total_fingers
    not_clients_num = total_clients - total_clients_num
    result = not_clients_num
    return result

print(solution())