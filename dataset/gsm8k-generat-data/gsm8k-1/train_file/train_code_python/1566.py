def solution():
    """Billy and Tiffany are having a contest to see how can run the most miles in a week. On Sunday, Monday, and Tuesday, Billy runs 1 mile each day and Tiffany runs 2 miles each day. On Wednesday, Thursday, and Friday, Billy runs 1 mile each day and Tiffany runs a 1/3 of a mile each day. On Saturday Tiffany assumes she's going to win and takes the day off. How many miles does Billy have to run on Saturday to tie Tiffany?"""
    billy_total = 6 # 1 mile for 3 days and 1 mile for 3 days
    tiffany_total = 6 + (2 * 3) + ((1/3) * 3) # 6 miles from first 6 days, 2 miles for 3 days, 1/3 mile for 3 days
    miles_to_tie = tiffany_total - billy_total # difference in miles
    result = miles_to_tie
    return result

print(solution())