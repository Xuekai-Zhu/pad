def solution():
    """Sally bought 3 photograph frames, each costing her $3. She paid with a $20 bill. How much change did she get?"""
    frames = 3
    cost_per_frame = 3
    total_cost = frames * cost_per_frame
    paid_with = 20
    change = paid_with - total_cost
    result = change
    return result

print(solution())