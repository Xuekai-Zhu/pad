def solution():
    # Calculate the total number of beavers in Canada
    num_beavers = 38 * 19

    # Calculate the total number of moose in Canada
    num_moose = num_beavers / 2

    # Convert the moose population to millions
    moose_population = num_moose / 1000000

    result = moose_population
    return result

print(solution())