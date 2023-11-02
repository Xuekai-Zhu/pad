def solution():
    # Given that Kiarra is twice as old as Bea and Kiarra is 30
    kiarra_age = 30
    bea_age = kiarra_age / 2

    # Job is 3 times older than Bea
    job_age = 3 * bea_age

    # Figaro is 7 years older than Job
    figaro_age = job_age + 7

    # Harry is half as old as Figaro
    harry_age = figaro_age / 2
    result = harry_age
    return result

print(solution())