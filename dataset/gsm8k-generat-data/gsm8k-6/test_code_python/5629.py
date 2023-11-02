def solution():
    # Calculate the percentage of the town that is immune in some way
    immune_percent = ((1/3) * 100) + ((1/3) * 100) - ((1/6) * 100)  # add the percentage of vaccinated and recovered individuals, but subtract the double-counted percentage of those who are both
    result = immune_percent
    return result

print(solution())