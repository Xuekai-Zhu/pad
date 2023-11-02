def solution():
    springfield_pop = 482653
    greenville_pop_diff = -119666

    # Calculate the population of Greenville
    greenville_pop = springfield_pop + greenville_pop_diff

    # Calculate the total population of Springfield and Greenville
    total_pop = springfield_pop + greenville_pop
    result = total_pop
    return result

print(solution())