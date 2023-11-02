def solution():
    hourly_wage = 9
    num_hours = 8

    num_restrung_racquets = 7
    restrung_racquet_pay = 15

    num_grommet_changes = 2
    grommet_change_pay = 10

    num_stencil_paints = 5
    stencil_paint_pay = 1

    # Calculate the total pay for stringing racquets
    restrung_racquet_total = restrung_racquet_pay * num_restrung_racquets

    # Calculate the total pay for changing grommets on racquets
    grommet_change_total = grommet_change_pay * num_grommet_changes

    # Calculate the total pay for painting stencils on racquet strings
    stencil_paint_total = stencil_paint_pay * num_stencil_paints

    # Calculate the total pay for all work done during the shift
    total_pay = (hourly_wage * num_hours) + restrung_racquet_total + grommet_change_total + stencil_paint_total
    result = total_pay
    return result

print(solution())