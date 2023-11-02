def solution():
    hourly_pay = 9  # Andy earns $9 per hour
    racquet_restring_pay = 15  # Andy earns $15 for each racquet he restrings
    grommet_change_pay = 10  # Andy earns $10 for changing out the grommets on a racquet
    stencil_paint_pay = 1  # Andy earns $1 for painting a stencil on the racquet strings
    hours_worked = 8  # Andy works an 8-hour shift
    racquets_restrung = 7  # Andy restrings 7 racquets during his shift
    grommets_changed = 2  # Andy changes 2 sets of racquet grommets
    stencils_painted = 5  # Andy paints 5 racquet stencils

    # Calculate the total pay for racquet stringing
    racquet_pay = racquet_restring_pay * racquets_restrung

    # Calculate the total pay for grommet changing
    grommet_pay = grommet_change_pay * grommets_changed

    # Calculate the total pay for stencil painting
    stencil_pay = stencil_paint_pay * stencils_painted

    # Calculate the total pay for the 8-hour shift
    total_pay = hourly_pay * hours_worked + racquet_pay + grommet_pay + stencil_pay
    result = total_pay
    return result

print(solution())