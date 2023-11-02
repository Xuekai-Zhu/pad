def solution():
    cross_time = 4 # in hours
    assistant_cost = 10 # per hour

    # Since Tom needs help both ways, we need to multiply the cross_time by 2
    total_time = cross_time * 2 

    # Calculate the total cost for the assistant for the entire trip
    total_cost = total_time * assistant_cost

    result = total_cost
    return result

print(solution())