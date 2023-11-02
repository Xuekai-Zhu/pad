def solution():
    """Tom goes to a combined undergrad and Ph.D. program. It takes 3 years to finish the BS and 5 years to finish the Ph.D. Tom finishes it in 3/4ths the time. How long does it take for him to finish?"""
    # Calculate the time it would take to finish the program without finishing early
    regular_time = 3 + 5

    # Calculate the time it took Tom to finish the program early
    early_time = regular_time * 3/4

    # Return the result
    result = early_time
    return result

print(solution())