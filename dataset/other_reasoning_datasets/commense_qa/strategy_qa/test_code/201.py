def solution():
    deaths_by_jokes = 2 # Chrysippus and King Martin
    deaths_by_rat_attacks = 300 # assuming an average of 30 per century for 10 centuries
    if deaths_by_jokes > deaths_by_rat_attacks:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())