def solution():
    """Antoine owns a strawberry farm that supplies strawberries to his local bakeries. The first bakery needs 2 sacks, the second bakery needs 4 sacks, and the third bakery needs 12 sacks of strawberries per week. How many sacks of strawberries does he need to supply all the bakeries in 4 weeks?"""
    bakery1 = 2
    bakery2 = 4
    bakery3 = 12
    total_sacks = (bakery1 + bakery2 + bakery3) * 4
    result = total_sacks
    return result

print(solution())