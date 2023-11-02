def solution():
    hourly_wage = 9  # dollars per hour
    racquet_restring = 15  # dollars per racquet restring
    grommet_change = 10  # dollars per grommet change
    stencil_paint = 1  # dollar per stencil paint

    # Calculate the total earnings for Andy during an 8-hour shift
    earnings_hourly = hourly_wage * 8
    earnings_racquet = racquet_restring * 7
    earnings_grommet = grommet_change * 2
    earnings_stencil = stencil_paint * 5
    total_earnings = earnings_hourly + earnings_racquet + earnings_grommet + earnings_stencil
    result = total_earnings
    return result

print(solution())