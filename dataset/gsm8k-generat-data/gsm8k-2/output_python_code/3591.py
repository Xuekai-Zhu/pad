def solution():
    """Tom goes to a combined undergrad and Ph.D. program. It takes 3 years to finish the BS and 5 years to finish the Ph.D. Tom finishes it in 3/4ths the time. How long does it take for him to finish?"""
    bs_time = 3
    phd_time = 5
    total_time = bs_time + phd_time
    actual_time = total_time * (3/4)
    result = actual_time
    return result

print(solution())