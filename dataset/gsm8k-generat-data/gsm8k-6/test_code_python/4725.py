def solution():
    # Calculate the number of beavers in Canada
    num_beavers = 38 * 1000000 / 19  # for every beaver there are 19 humans

    # Calculate the number of moose in Canada
    num_moose = num_beavers / 2  # for every moose there are two beavers

    # Convert the number of moose to millions
    num_moose_millions = num_moose / 1000000

    result = num_moose_millions
    return result

print(solution())