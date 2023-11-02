def solution():
    """Andy works in the pro shop at a tennis resort, where he earns $9 an hour. In addition to this, he gets paid $15 for each racquet he restrings, $10 for changing out the grommets on a racquet, and $1 for painting a stencil on the racquet strings. How much does he earn (before taxes) during an 8-hour shift if he strings 7 racquets, changes 2 sets of grommets, and paints 5 stencils?"""
    # Define the hourly rate, and the additional pay rates
    HOURLY_RATE = 9
    RESTRING_RATE = 15
    GROMMET_RATE = 10
    STENCIL_RATE = 1

    # Define the number of racquets restrung, grommets changed, and stencils painted
    racquets_restrung = 7
    grommets_changed = 2
    stencils_painted = 5

    # Calculate the total pay for restrung racquets, changed grommets, and painted stencils
    total_restring_pay = racquets_restrung * RESTRING_RATE
    total_grommet_pay = grommets_changed * GROMMET_RATE
    total_stencil_pay = stencils_painted * STENCIL_RATE

    # Calculate the total pay for the shift
    total_pay = (HOURLY_RATE * 8) + total_restring_pay + total_grommet_pay + total_stencil_pay

    # return the result
    result = total_pay
    return result

print(solution())