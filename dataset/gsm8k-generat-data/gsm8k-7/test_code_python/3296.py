def solution():
    time_to_work = 2  # hours
    time_to_work_and_back = time_to_work * 2  # hours
    packs_per_time = 10
    num_packs = 50

    # Calculate the cost of one pack of snacks
    cost_per_pack = time_to_work_and_back * packs_per_time

    # Calculate the total cost of all packs of snacks
    total_cost = cost_per_pack * num_packs
    result = total_cost
    return result

print(solution())