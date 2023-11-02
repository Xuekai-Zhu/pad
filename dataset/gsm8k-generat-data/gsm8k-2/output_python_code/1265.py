def solution():
    """Aida has twice as many dolls as Sophie, and Sophie has twice as many dolls as Vera. How many dolls do Aida, Sophie, and Vera have combined if Vera has 20 dolls?"""
    vera_dolls = 20
    sophie_dolls = 2 * vera_dolls
    aida_dolls = 2 * sophie_dolls
    total_dolls = vera_dolls + sophie_dolls + aida_dolls
    result = total_dolls
    return result

print(solution())