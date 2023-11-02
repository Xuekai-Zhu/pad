def solution():
    # Calculate the total number of washing machines in the container before removal
    total_washing_machines = 10 * 6 * 4  # 10 crates, 6 boxes per crate, 4 washing machines per box

    # Calculate the number of washing machines removed
    removed_washing_machines = 6 * 4 * 1  # 1 washing machine removed from each of the 6 boxes in each crate

    # Calculate the total number of washing machines left in the container after removal
    remaining_washing_machines = total_washing_machines - removed_washing_machines

    result = removed_washing_machines
    return result

print(solution())