def solution():
    # Calculate the number of miles last year's winner walked
    miles_last_year = 44 / 4  # walkers earned $4 a mile

    # Calculate the number of miles Elroy needs to walk to collect the same amount of money
    miles_this_year = 44 / 2.75  # walkers earn $2.75 a mile
    
    # Calculate the difference in miles between Elroy and last year's winner
    difference = miles_this_year - miles_last_year
    result = difference
    return result

print(solution())