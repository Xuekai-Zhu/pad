def solution():
    """Trace has five shopping bags that weigh the same amount as Gordon’s two shopping bags. One of Gordon’s shopping bags weighs three pounds and the other weighs seven. Trace’s shopping bags all weigh the same amount. How many pounds does one of Trace’s bags weigh?"""
    # Calculate the total weight of Gordon's shopping bags
    gordon_total_weight = 3 + 7

    # Calculate the weight of one of Trace's shopping bags
    trace_bag_weight = gordon_total_weight / 5

    # Display the weight of one of Trace's shopping bags
    result = trace_bag_weight
    return result

print(solution())