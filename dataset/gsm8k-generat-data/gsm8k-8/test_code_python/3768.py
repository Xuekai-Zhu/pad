def solution():
    # Calculate the total number of washing machines in the container before removal
    total_wash_machines_before = 10 * 6 * 4

    # Calculate the total number of washing machines in the container after removal
    total_wash_machines_after = 10 * 6 * 3

    # Calculate the number of washing machines removed
    wash_machines_removed = total_wash_machines_before - total_wash_machines_after
    result = wash_machines_removed
    return result

print(solution())