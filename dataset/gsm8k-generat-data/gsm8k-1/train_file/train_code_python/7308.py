def solution():
    """Enid and Aaron are knitting clothes for their store. Aaron makes 10 scarves and 5 sweaters, and Enid makes 8 sweaters. If a scarf uses 3 balls of wool and a sweater uses 4 balls of wool, how many balls of wool did Enid and Aaron use in total?"""
    aaron_scarves = 10
    aaron_sweaters = 5
    enid_sweaters = 8
    scarves_wool = 3
    sweaters_wool = 4
    total_wool = (aaron_scarves * scarves_wool) + (aaron_sweaters * sweaters_wool) + (enid_sweaters * sweaters_wool)
    result = total_wool
    return result

print(solution())