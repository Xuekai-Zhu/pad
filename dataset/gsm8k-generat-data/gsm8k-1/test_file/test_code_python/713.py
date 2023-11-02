def solution():
    """A pencil cost $0.50, and an eraser cost $0.25. If you bought 6 pencils and 8 erasers and paid $10, how much change would you get?"""
    pencil_cost = 0.5
    eraser_cost = 0.25
    num_pencils = 6
    num_erasers = 8
    total_cost = (pencil_cost * num_pencils) + (eraser_cost * num_erasers)
    change = 10 - total_cost
    result = change
    return result

print(solution())