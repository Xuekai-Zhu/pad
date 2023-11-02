def solution():
    """Antoine owns a strawberry farm that supplies strawberries to his local bakeries. The first bakery needs 2 sacks, the second bakery needs 4 sacks, and the third bakery needs 12 sacks of strawberries per week. How many sacks of strawberries does he need to supply all the bakeries in 4 weeks?"""
    # Define the number of sacks needed by each bakery per week
    bakery1_sacks_per_week = 2
    bakery2_sacks_per_week = 4
    bakery3_sacks_per_week = 12

    # Calculate the total number of sacks needed by all bakeries for 4 weeks
    total_sacks = (bakery1_sacks_per_week + bakery2_sacks_per_week + bakery3_sacks_per_week) * 4

    result = total_sacks
    return result

print(solution())