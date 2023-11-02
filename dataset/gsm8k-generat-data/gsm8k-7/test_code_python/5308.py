def solution():
    gordon_bag1 = 3
    gordon_bag2 = 7
    trace_bags = 5

    # Calculate the total weight of Gordon's shopping bags
    total_gordon_weight = gordon_bag1 + gordon_bag2

    # Calculate the weight of each of Trace's shopping bags
    each_trace_weight = total_gordon_weight / trace_bags
    result = each_trace_weight
    return result

print(solution())