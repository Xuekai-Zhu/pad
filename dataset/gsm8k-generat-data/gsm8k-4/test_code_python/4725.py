def solution():
    """In Canada, for every moose there are two beavers, and for every beaver there are 19 humans. If there are 38 million people in Canada, what is the moose population of Canada, in millions?"""
    # Define the number of humans in Canada
    humans = 38000000

    # Calculate the number of beavers in Canada
    beavers = humans / 19

    # Calculate the number of moose in Canada
    moose = beavers / 2

    # Convert the moose population to millions
    moose_millions = moose / 1000000

    # round off the moose population to 2 decimal places
    result = round(moose_millions, 2)
    return result

print(solution())