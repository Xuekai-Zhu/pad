def solution():
    """Billy and George are picking dandelions. At first, Billy picks 36 and then George picks 1/3 as many as Billy. When they see the pile, they each decide to pick 10 more each. How many have they picked on average?"""
    # Define the initial number of dandelions picked by Billy
    billy_picks = 36

    # Define the number of dandelions picked by George as a fraction of Billy's picks
    george_fraction = 1/3

    # Calculate the number of dandelions picked by George
    george_picks = billy_picks * george_fraction

    # Calculate the total number of dandelions before they pick 10 more each
    total_picks = billy_picks + george_picks

    # Calculate the new total number of dandelions after they each pick 10 more
    new_total_picks = total_picks + 10*2

    # Calculate the average number of dandelions they picked
    average_picks = new_total_picks / 2

    # Return the result
    result = average_picks
    return result

print(solution())