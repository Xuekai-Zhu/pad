def solution():
    """Trace has five shopping bags that weigh the same amount as Gordon’s two shopping bags. One of Gordon’s shopping bags weighs three pounds and the other weighs seven. Trace’s shopping bags all weigh the same amount. How many pounds does one of Trace’s bags weigh?"""
    # Define the weights of Gordon's shopping bags
    gordon_bag1_weight = 3
    gordon_bag2_weight = 7

    # Determine the total weight of Gordon's shopping bags
    total_gordon_weight = gordon_bag1_weight + gordon_bag2_weight

    # Determine the weight of one of Trace's shopping bags
    trace_bag_weight = total_gordon_weight / 5

    result = trace_bag_weight
    return result

print(solution())