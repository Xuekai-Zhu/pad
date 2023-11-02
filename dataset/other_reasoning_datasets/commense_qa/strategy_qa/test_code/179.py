def solution():
    new_york_harbor_discovery_year = 1500
    donald_trump_is_a_failed_businessman = True
    donald_trump_makes_outrageous_claims = True
    if donald_trump_is_a_failed_businessman and donald_trump_makes_outrageous_claims:
        result = "no"
    else:
        result = "The idea for New York Harbor was discovered in {} before Donald Trump's time.".format(new_york_harbor_discovery_year)
    return result

print(solution())