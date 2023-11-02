def solution():
    """Nunzio eats three pieces of pizza every day for lunch. If a piece of pizza represents one-eighth of the entire pie, then how many pizzas does Nunzio eat in 72 days?"""
    pieces_per_day = 3
    days = 72
    pieces_per_pie = 8
    total_pies = (pieces_per_day * days) / pieces_per_pie
    result = total_pies
    return result

print(solution())