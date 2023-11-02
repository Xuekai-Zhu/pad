def solution():
    """Billy and George are picking dandelions. At first, Billy picks 36 and then George picks 1/3 as many as Billy. When they see the pile, they each decide to pick 10 more each. How many have they picked on average?"""
    billy_picked = 36
    george_picked = billy_picked / 3
    total_picked = billy_picked + george_picked
    total_picked += 20
    average_picked = total_picked / 2
    result = average_picked
    return result

print(solution())