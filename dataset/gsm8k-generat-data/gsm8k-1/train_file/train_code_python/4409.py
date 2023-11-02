def solution():
    """Bob grew corn in his garden and is ready to harvest it. He has 5 rows of corn, and each row has 80 corn stalks. About every 8 corn stalks will produce a bushel of corn. How many bushels of corn will Bob harvest?"""
    rows_of_corn = 5
    corn_per_row = 80
    corn_stalks_per_bushel = 8
    total_corn_stalks = rows_of_corn * corn_per_row
    bushels_of_corn = total_corn_stalks // corn_stalks_per_bushel
    result = bushels_of_corn
    return result

print(solution())