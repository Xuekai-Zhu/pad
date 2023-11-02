def solution():
    """Trace has five shopping bags that weigh the same amount as Gordon’s two shopping bags. One of Gordon’s shopping bags weighs three pounds and the other weighs seven. Trace’s shopping bags all weigh the same amount. How many pounds does one of Trace’s bags weigh?"""
    gordon_total_weight = 3 + 7
    trace_one_bag_weight = gordon_total_weight / 5
    result = trace_one_bag_weight
    return result

print(solution())