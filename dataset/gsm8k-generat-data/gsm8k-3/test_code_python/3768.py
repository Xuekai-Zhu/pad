def solution():
    """In a shipping container, there are 10 crates. Each crate is filled with 6 boxes and each box is filled with 4 washing machines. A worker removes 1 washing machine from each box. There are no other changes. How many washing machines were removed from the shipping container?"""
    # Calculate the total number of washing machines in the container
    total_washing_machines = 10 * 6 * 4

    # Calculate the number of washing machines removed
    removed_washing_machines = 6 * 4 * 10

    # Display the number of washing machines removed
    result = removed_washing_machines
    return result

print(solution())