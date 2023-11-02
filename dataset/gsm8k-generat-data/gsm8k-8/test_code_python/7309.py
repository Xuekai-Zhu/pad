def solution():
    # Calculate the total number of balls of wool used by Aaron
    aaron_scarf_wool = 10 * 3
    aaron_sweater_wool = 5 * 4
    aaron_total_wool = aaron_scarf_wool + aaron_sweater_wool

    # Calculate the total number of balls of wool used by Enid
    enid_sweater_wool = 8 * 4

    # Calculate the total number of balls of wool used by both of them
    total_wool_used = aaron_total_wool + enid_sweater_wool
    result = total_wool_used
    return result

print(solution())