def solution():
    billy_miles = 0
    tiffany_miles = 0
    
    # Calculate total miles for Sunday, Monday, and Tuesday
    billy_miles += 3
    tiffany_miles += 6
    
    # Calculate total miles for Wednesday, Thursday, and Friday
    billy_miles += 3
    tiffany_miles += 1
    
    # Calculate how many miles Billy needs to run on Saturday to tie Tiffany
    miles_to_tie = tiffany_miles - billy_miles
    
    result = miles_to_tie
    return result

print(solution())