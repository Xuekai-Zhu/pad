def solution():
    """Andy works in the pro shop at a tennis resort, where he earns $9 an hour. In addition to this, he gets paid $15 for each racquet he restrings, $10 for changing out the grommets on a racquet, and $1 for painting a stencil on the racquet strings. How much does he earn (before taxes) during an 8-hour shift if he strings 7 racquets, changes 2 sets of grommets, and paints 5 stencils?"""
    hourly_wage = 9
    racquet_restringing_payment = 15
    grommet_changing_payment = 10
    stencil_painting_payment = 1
    total_hourly_payment = hourly_wage * 8
    total_racquet_restringing_payment = racquet_restringing_payment * 7
    total_grommet_changing_payment = grommet_changing_payment * 2
    total_stencil_painting_payment = stencil_painting_payment * 5
    total_payment = total_hourly_payment + total_racquet_restringing_payment + total_grommet_changing_payment + total_stencil_painting_payment
    result = total_payment
    return result

print(solution())