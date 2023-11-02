def solution():
    """Andy works in the pro shop at a tennis resort, where he earns $9 an hour. In addition to this, he gets paid $15 for each racquet he restrings, $10 for changing out the grommets on a racquet, and $1 for painting a stencil on the racquet strings. How much does he earn (before taxes) during an 8-hour shift if he strings 7 racquets, changes 2 sets of grommets, and paints 5 stencils?"""
    # Define the pay rates for each task
    HOURLY_RATE = 9
    RESTRING_PAY = 15
    GROMMET_PAY = 10
    STENCIL_PAY = 1

    # Define the number of each task completed
    num_restrings = 7
    num_grommet_changes = 2
    num_stencil_paints = 5

    # Calculate the pay for each task
    restrings_pay = num_restrings * RESTRING_PAY
    grommet_pay = num_grommet_changes * GROMMET_PAY
    stencil_pay = num_stencil_paints * STENCIL_PAY

    # Calculate the total pay for the shift
    total_pay = (HOURLY_RATE * 8) + restrings_pay + grommet_pay + stencil_pay

    # Display the total pay for the shift
    result = total_pay
    return result

print(solution())