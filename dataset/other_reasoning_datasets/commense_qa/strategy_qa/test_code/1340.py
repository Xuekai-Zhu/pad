def solution():
    robusto = "cigar"
    zoo_rules = ["no feeding the animals", "no smoking"]
    nearby_precinct_distance = 11 # in minutes
    if robusto in zoo_rules or nearby_precinct_distance < 15:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())