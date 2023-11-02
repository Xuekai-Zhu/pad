def solution():
    # Calculate the total number of beads
    total_beads = 23 + 16

    # Divide the total into 3 equal parts
    equal_parts = total_beads / 3

    # Remove some beads from each part
    removed_beads = equal_parts - 6

    # Calculate how many beads were removed from each part
    removed_from_each_part = removed_beads / 2

    result = removed_from_each_part
    return result

print(solution())