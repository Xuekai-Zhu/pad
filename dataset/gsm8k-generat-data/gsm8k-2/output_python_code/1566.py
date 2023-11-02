def solution():
    """Billy and Tiffany are having a contest to see how can run the most miles in a week. On Sunday, Monday, and Tuesday, Billy runs 1 mile each day and Tiffany runs 2 miles each day. On Wednesday, Thursday, and Friday, Billy runs 1 mile each day and Tiffany runs a 1/3 of a mile each day. On Saturday Tiffany assumes she's going to win and takes the day off. How many miles does Billy have to run on Saturday to tie Tiffany?"""
    billy_miles = 0
    tiffany_miles = 0
    # Sunday, Monday, Tuesday
    billy_miles += 3
    tiffany_miles += 6
    # Wednesday, Thursday, Friday
    billy_miles += 3
    tiffany_miles += 1
    # Saturday
    billy_miles_to_tie = tiffany_miles - billy_miles
    result = billy_miles_to_tie

    return result

print(solution())