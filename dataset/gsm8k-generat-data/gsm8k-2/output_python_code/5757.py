def solution():
    """Billy and George are picking dandelions. At first, Billy picks 36 and then George picks 1/3 as many as Billy. When they see the pile, they each decide to pick 10 more each. How many have they picked on average?"""
    billy_picks = 36
    george_picks = (1/3) * billy_picks
    total_picks = billy_picks + george_picks
    total_picks += 2*10 # adding 10 picks for each of them
    average_picks = total_picks / 2
    result = average_picks
    return result

print(solution())