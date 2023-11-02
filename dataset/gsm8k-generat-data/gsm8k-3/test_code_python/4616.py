def solution():
    """Antoine owns a strawberry farm that supplies strawberries to his local bakeries. The first bakery needs 2 sacks, the second bakery needs 4 sacks, and the third bakery needs 12 sacks of strawberries per week. How many sacks of strawberries does he need to supply all the bakeries in 4 weeks?"""
    # Define the number of sacks needed per week by each bakery
    bakery1 = 2
    bakery2 = 4
    bakery3 = 12

    # Calculate the total number of sacks needed for all the bakeries in a week
    total_per_week = bakery1 + bakery2 + bakery3

    # Calculate the total number of sacks needed for all the bakeries in 4 weeks
    total_per_month = total_per_week * 4

    # Display the total number of sacks needed
    result = total_per_month
    return result

print(solution())