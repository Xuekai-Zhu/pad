def solution():
    """Agatha has some money to spend on a new bike. She spends $15 on the frame, and $25 on the front wheel. If she has $20 left to spend on a seat and handlebar tape, how much money, in dollars, did she have at first?"""
    frame_cost = 15
    front_wheel_cost = 25
    remaining_money = 20
    total_cost = frame_cost + front_wheel_cost + remaining_money
    initial_money = total_cost + remaining_money
    result = initial_money
    return result

print(solution())