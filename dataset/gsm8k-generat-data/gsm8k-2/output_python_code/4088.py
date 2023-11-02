def solution():
    """Martine has 6 more than twice as many peaches as Benjy. Benjy has one-third as many peaches as Gabrielle. If Martine has 16 peaches, how many does Gabrielle have?"""
    martine_peaches = 16
    benjy_peaches = (martine_peaches - 6) / 2
    gabrielle_peaches = benjy_peaches * 3
    result = gabrielle_peaches
    return result

print(solution())