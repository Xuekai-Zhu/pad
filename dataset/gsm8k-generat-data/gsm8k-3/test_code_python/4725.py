def solution():
    """In Canada, for every moose there are two beavers, and for every beaver there are 19 humans.  If there are 38 million people in Canada, what is the moose population of Canada, in millions?"""
    # Calculate the number of beavers in Canada
    beavers = 38 * 1000000 / 19

    # Calculate the number of moose in Canada
    moose = beavers / 2

    # Convert the moose population to millions
    moose_millions = moose / 1000000

    # Display the moose population in millions
    result = moose_millions
    return result

print(solution())