def solution():
    # Define the years Mitterrand and Obama were in office
    mitterrand_years = range(1981, 1996)
    obama_years = range(2009, 2018)
    # Check if the years overlapped and if they could have met
    if set(mitterrand_years).intersection(obama_years) and mitterrand_years[-1] <= obama_years[0]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())