def solution():
    """In a shipping container, there are 10 crates. Each crate is filled with 6 boxes and each box is filled with 4 washing machines. A worker removes 1 washing machine from each box. There are no other changes. How many washing machines were removed from the shipping container?"""
    crates = 10
    boxes_per_crate = 6
    machines_per_box = 4
    machines_removed_per_box = 1
    total_machines = crates * boxes_per_crate * machines_per_box
    total_machines_removed = crates * boxes_per_crate * machines_removed_per_box
    machines_removed = total_machines - (total_machines_removed)
    result = machines_removed
    return result

print(solution())