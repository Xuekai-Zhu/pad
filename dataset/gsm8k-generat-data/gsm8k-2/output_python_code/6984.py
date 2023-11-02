def solution():
    """Andy works in the pro shop at a tennis resort, where he earns $9 an hour. In addition to this, he gets paid $15 for each racquet he restrings,
    $10 for changing out the grommets on a racquet, and $1 for painting a stencil on the racquet strings.
    How much does he earn (before taxes) during an 8-hour shift if he strings 7 racquets, changes 2 sets of grommets, and paints 5 stencils?"""
    hourly_rate = 9
    restrung_racquets = 7
    grommet_sets_changed = 2
    stencils_painted = 5
    restrung_racquet_pay = 15 * restrung_racquets
    grommet_pay = 10 * grommet_sets_changed
    stencil_pay = 1 * stencils_painted
    total_pay = (hourly_rate * 8) + restrung_racquet_pay + grommet_pay + stencil_pay
    result = total_pay
    return result

print(solution())