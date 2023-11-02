def solution():
    
    # Define the number of beds and king size bed used per week
    beds_per_week = 4
    king_size_beds_per_week = 1

    # Define the number of sets of sheets Greg can wash per week
    twin_sets_per_week = 2
    king_sets_per_week = 1

    # Define the number of weeks in a year
    weeks_per_year = 52

    # Calculate the total number of sheets Greg can clean in a year
    total_sheets = (beds_per_week * beds_per_week * weeks_per_year) * sheets_per_beds_per_week * weeks_per_year

    # Calculate the number of loads of laundry Greg can do in a year
    loads_per_year = total_sheets / twin_sets_per_week * weeks_per_year

    # Return the result
    result = loads_per_year
    return result

print(solution())