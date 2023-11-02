def solution():
    # Calculate the total number of washing machines in the container before removal
    total_machines = 10 * 6 * 4  # 10 crates, each crate has 6 boxes, each box has 4 washing machines
    # Calculate the total number of washing machines after removal
    remaining_machines = 10 * 6 * (4-1)  # 1 washing machine removed from each box
    # Calculate the number of washing machines removed
    removed_machines = total_machines - remaining_machines
    result = removed_machines
    return result

print(solution())