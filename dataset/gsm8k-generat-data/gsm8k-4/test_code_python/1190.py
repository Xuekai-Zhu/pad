def solution():
    """Kiarra is twice as old as Bea. Job is 3 times older than Bea. Figaro is 7 years older than Job. Harry is half as old as Figaro. If Kiarra is 30, how old is Harry?"""
    # Define Kiarra's age
    kiarra_age = 30

    # Calculate Bea's age
    bea_age = kiarra_age / 2

    # Calculate Job's age
    job_age = 3 * bea_age

    # Calculate Figaro's age
    figaro_age = job_age + 7

    # Calculate Harry's age
    harry_age = figaro_age / 2

    # Return Harry's age
    result = harry_age
    return result

print(solution())