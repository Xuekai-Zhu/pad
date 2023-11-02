def solution():
    """Kiarra is twice as old as Bea. Job is 3 times older than Bea. Figaro is 7 years older than Job. Harry is half as old as Figaro. If Kiarra is 30, how old is Harry?"""
    kiarra_age = 30
    bea_age = kiarra_age / 2
    job_age = 3 * bea_age
    figaro_age = job_age + 7
    harry_age = figaro_age / 2
    result = harry_age
    return result

print(solution())