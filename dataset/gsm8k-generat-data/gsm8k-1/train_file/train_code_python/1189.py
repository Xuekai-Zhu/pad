def solution():
    """
    Kiarra is twice as old as Bea. Job is 3 times older than Bea. Figaro is 7 years older than Job. Harry is half as old as Figaro. 
    If Kiarra is 30, how old is Harry?
    """
    kiarra = 30
    bea = kiarra / 2
    job = 3 * bea
    figaro = job + 7
    harry = figaro / 2
    result = harry
    return result

print(solution())