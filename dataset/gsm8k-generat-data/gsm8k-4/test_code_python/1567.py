def solution():
    """Billy and Tiffany are having a contest to see how can run the most miles in a week. On Sunday, Monday, and Tuesday, Billy runs 1 mile each day and Tiffany runs 2 miles each day. On Wednesday, Thursday, and Friday, Billy runs 1 mile each day and Tiffany runs a 1/3 of a mile each day. On Saturday Tiffany assumes she's going to win and takes the day off. How many miles does Billy have to run on Saturday to tie Tiffany?"""
    # Calculate the total miles run by Billy from Sunday to Friday
    billy_miles = 1 + 1 + 1 + 1 + 1 + 1

    # Calculate the total miles run by Tiffany from Sunday to Friday
    tiffany_miles = 2 + 2 + 2 + 1/3 + 1/3 + 1/3

    # Determine how many miles Billy needs to run on Saturday to tie Tiffany
    saturday_miles = tiffany_miles - billy_miles

    # Return the result
    result = round(saturday_miles, 2)
    return result

print(solution())