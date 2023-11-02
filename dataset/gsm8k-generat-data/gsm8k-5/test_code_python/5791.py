def solution():
    last_year_collection = 44  # Last year's winner collected $44
    last_year_salary_per_mile = 4  # Last year, walkers earned $4 per mile
    this_year_salary_per_mile = 2.75  # This year, walkers earn $2.75 per mile

    # Calculate the number of miles last year's winner walked
    last_year_miles = last_year_collection / last_year_salary_per_mile

    # Calculate the amount of money Elroy needs to collect to tie last year's winner
    elroy_collection = last_year_collection

    # Calculate the number of miles Elroy needs to walk to collect the same amount of money
    elroy_miles = elroy_collection / this_year_salary_per_mile

    # Calculate the difference in miles between Elroy and last year's winner
    difference = elroy_miles - last_year_miles
    result = difference
    return result

print(solution())