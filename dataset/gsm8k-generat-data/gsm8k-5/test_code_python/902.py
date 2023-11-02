def solution():
    total_straws = 300  # Troy had 300 straws
    adult_pigs_straws = (3/5) * total_straws  # Troy fed 3/5 of the straws to adult pigs
    piglets_straws = adult_pigs_straws / 2  # An equal number of straws were given to piglets

    # Calculate how many straws each piglet ate
    straws_per_piglet = piglets_straws / 20
    result = straws_per_piglet
    return result

print(solution())