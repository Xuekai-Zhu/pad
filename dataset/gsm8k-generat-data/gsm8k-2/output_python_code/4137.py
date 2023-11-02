def solution():
    """Agatha has some money to spend on a new bike. She spends $15 on the frame, and $25 on the front wheel. If she has $20 left to spend on a seat and handlebar tape, how much money, in dollars, did she have at first?"""
    spent_money = 15 + 25 + 20  # total money spent so far
    initial_money = spent_money * 2  # double the spent money
    result = initial_money
    return result

print(solution())