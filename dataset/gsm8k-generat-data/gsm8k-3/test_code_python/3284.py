def solution():
    """Antonella has ten Canadian coins in her purse that are either loonies or toonies. A loonie equals $1 and a toonie equals $2. If she bought a $3 Frappuccino and still has $11, how many toonies did she initially have?"""
    # Set up the equation with l representing loonies and t representing toonies
    # l + t = 10 (she has ten coins)
    # 1l + 2t - 3 = x (she spent $3 and has $x left, which we know is 11)
    # We can simplify the second equation to 1l + 2t = x+3 = 14
    # Now we can solve for t: t = (14-l)/2
    for l in range(11):
        t = (14-l)/2
        if t == int(t):
            result = int(t)
            return result
    return None

print(solution())