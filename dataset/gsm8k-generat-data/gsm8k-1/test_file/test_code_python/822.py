def solution():
    """On Easter Sunday Cindy went to the city park to participate in the Easter Egg Hunt, and ended up with a basket full of eggs. She had 5 green ones, twice as many blue ones as green ones, one fewer pink eggs than blue eggs, and one-third as many yellow eggs as pink eggs. How many eggs did Cindy have altogether?"""
    green_eggs = 5
    blue_eggs = green_eggs * 2
    pink_eggs = blue_eggs - 1
    yellow_eggs = pink_eggs / 3
    total_eggs = green_eggs + blue_eggs + pink_eggs + yellow_eggs
    result = total_eggs
    return result

print(solution())