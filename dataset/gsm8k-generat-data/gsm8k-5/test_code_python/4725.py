def solution():
    # Calculate the number of beavers in Canada
    num_beavers = 38 * 1000000 / 19

    # Calculate the number of moose in Canada
    num_moose = num_beavers / 2
    result = num_moose / 1000000
    return result

print(solution())