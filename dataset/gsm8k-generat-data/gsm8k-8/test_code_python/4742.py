def solution():
    # Calculate the total number of relatives
    num_parents = 2
    num_brothers = 3
    num_nephews = 2 * num_brothers * 2  # 2 children per married brother
    total_relatives = num_parents + num_brothers + num_nephews

    # Calculate the cost to send one package to each relative
    cost_per_relative = 5

    # Calculate the total cost to send all gifts by mail
    total_cost = total_relatives * cost_per_relative
    result = total_cost
    return result

print(solution())