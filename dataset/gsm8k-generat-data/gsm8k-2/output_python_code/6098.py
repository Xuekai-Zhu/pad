def solution():
    """Rene has three times as many dolls as her sister, while her sister has two more dolls than their grandmother. If their grandmother has 50 dolls, how many dolls do they have altogether?"""
    grandmother_dolls = 50
    sister_dolls = grandmother_dolls + 2
    rene_dolls = 3 * sister_dolls
    total_dolls = grandmother_dolls + sister_dolls + rene_dolls
    result = total_dolls
    return result

print(solution())