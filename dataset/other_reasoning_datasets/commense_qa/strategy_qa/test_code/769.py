def solution():
    wagner_death_year = 1883
    nazi_established_year = 1919
    # Check if Wagner was alive when the Nazi Party was established
    if wagner_death_year < nazi_established_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())