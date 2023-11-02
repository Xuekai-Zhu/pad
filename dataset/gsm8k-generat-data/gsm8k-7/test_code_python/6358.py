def solution():
    total_juice_cost = 10
    num_juices = 5
    total_sandwich_cost = 6
    num_sandwiches = 2

    # Calculate the cost of one juice
    one_juice_cost = total_juice_cost / num_juices

    # Calculate the cost of one sandwich
    one_sandwich_cost = total_sandwich_cost / num_sandwiches

    # Calculate the total cost of one juice and one sandwich
    total_cost = one_juice_cost + one_sandwich_cost
    result = total_cost
    return result

print(solution())