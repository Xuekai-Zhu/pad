def solution():
    
    # Define the number of sheets Greg puts on each type of bed
    twin_beds = 4
    king_beds = 1

    # Calculate the number of sheets Greg puts on each type of bed per week
    total_twin_beds = twin_beds * 2
    total_king_beds = king_beds * 1

    # Calculate the number of sheets Greg puts on each type of bed per week
    total_sheets_per_week = total_twin_beds + total_king_beds

    # Calculate the number of loads of laundry Greg does in a year
    loads_per_year = total_sheets_per_week * 52

    # Display the number of loads of laundry Greg does in a year
    result = loads_per_year
    return result

print(solution())