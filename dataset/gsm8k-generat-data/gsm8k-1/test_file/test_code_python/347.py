def solution():
    """April is donating plant pots to a local school for their new garden. They ask for 30 plant pots for the daisies, and twice as many for the roses. April had already bought 100 plant pots from the garden center before she knew how many she needed. How many plant pots does April have left over?"""
    daisy_pots = 30
    rose_pots = daisy_pots * 2
    total_pots_needed = daisy_pots + rose_pots
    pots_bought = 100
    pots_left = pots_bought - total_pots_needed
    result = pots_left
    return result

print(solution())