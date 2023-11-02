def solution():
    """Antoine owns a strawberry farm that supplies strawberries to his local bakeries. The first bakery needs 2 sacks, the second bakery needs 4 sacks, and the third bakery needs 12 sacks of strawberries per week. How many sacks of strawberries does he need to supply all the bakeries in 4 weeks?"""
    bakery_1 = 2
    bakery_2 = 4
    bakery_3 = 12
    total_weeks = 4
    total_strawberries = (bakery_1 + bakery_2 + bakery_3) * total_weeks
    result = total_strawberries
    return result

print(solution())