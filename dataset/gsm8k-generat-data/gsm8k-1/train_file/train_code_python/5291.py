def solution():
    """One afternoon, Rachelle, Gretchen and Rocky threw pennies into the fountain and made wishes. Rachelle threw 180 pennies into the fountain. Gretchen threw half as many pennies into the fountain as Rachelle and Rocky threw in one-third as many pennies as Gretchen. What was the total number of pennies thrown into the fountain by the three of them?"""
    rachelle_pennies = 180
    gretchen_pennies = rachelle_pennies / 2
    rocky_pennies = gretchen_pennies / 3
    total_pennies = rachelle_pennies + gretchen_pennies + rocky_pennies
    result = total_pennies
    return result

print(solution())