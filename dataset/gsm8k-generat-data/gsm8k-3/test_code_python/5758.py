def solution():
    """Billy and George are picking dandelions. At first, Billy picks 36 and then George picks 1/3 as many as Billy. When they see the pile, they each decide to pick 10 more each. How many have they picked on average?"""
    # Calculate how many dandelions George picked
    george_picks = 36 * (1/3)

    # Calculate the total number of dandelions they picked before picking more
    total_picks = 36 + george_picks

    # Add the additional picks
    total_picks += 20

    # Calculate the average number of dandelions they picked
    average_picks = total_picks / 2

    # Display the average number of dandelions they picked
    result = average_picks
    return result

print(solution())