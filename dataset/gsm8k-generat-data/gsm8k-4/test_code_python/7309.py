def solution():
    """Enid and Aaron are knitting clothes for their store. Aaron makes 10 scarves and 5 sweaters, and Enid makes 8 sweaters. If a scarf uses 3 balls of wool and a sweater uses 4 balls of wool, how many balls of wool did Enid and Aaron use in total?"""
    # Calculate the number of balls of wool Aaron used
    aaron_scarf_wool = 10 * 3
    aaron_sweater_wool = 5 * 4
    aaron_total_wool = aaron_scarf_wool + aaron_sweater_wool

    # Calculate the number of balls of wool Enid used
    enid_sweater_wool = 8 * 4

    # Calculate the total number of balls of wool used by both of them
    total_wool = aaron_total_wool + enid_sweater_wool

    # return the result
    return total_wool

print(solution())