def solution():
    """Tom goes to a combined undergrad and Ph.D. program.  It takes 3 years to finish the BS and 5 years to finish the Ph.D.  Tom finishes it in 3/4ths the time.  How long does it take for him to finish?"""
    # Calculate the time it takes to finish the BS and Ph.D. separately
    bs_time = 3
    phd_time = 5
    total_time = bs_time + phd_time

    # Calculate the time it takes for Tom to finish in 3/4ths the time
    tom_time = total_time * 3/4

    # Display the time it takes for Tom to finish
    result = tom_time
    return result

print(solution())