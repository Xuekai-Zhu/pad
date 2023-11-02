def solution():
    """Jane is sewing sequins onto her trapeze artist costume. She sews 6 rows of 8 blue sequins each, 5 rows of 12 purple sequins each, and 9 rows of 6 green sequins each. How many sequins does she add total?"""
    blue_sequins = 6 * 8
    purple_sequins = 5 * 12
    green_sequins = 9 * 6
    total_sequins = blue_sequins + purple_sequins + green_sequins
    result = total_sequins
    return result

print(solution())