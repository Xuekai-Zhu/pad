def solution():
   berets_from_one_spool = 3
    spools_of_red_yarn = 12
    spools_of_black_yarn = 15
    spools_of_blue_yarn = 6
    total_spools = spools_of_red_yarn + spools_of_black_yarn + spools_of_blue_yarn
    berets_possible = total_spools / berets_from_one_spool
    result = berets_possible
    return result

print(solution())