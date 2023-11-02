def solution():
    num_wombats = 9
    wombat_claws = 4

    num_rheas = 3
    rhea_claws = 1

    # Calculate the total number of times Carson gets clawed by wombats
    wombat_claw_total = num_wombats * wombat_claws

    # Calculate the total number of times Carson gets clawed by rheas
    rhea_claw_total = num_rheas * rhea_claws

    # Calculate the total number of times Carson gets clawed
    total_claws = wombat_claw_total + rhea_claw_total
    result = total_claws
    return result

print(solution())