def solution():
    soul_calibur_sword = "zweihander"
    gladiator_sword = "gladius"
    hands_to_wield_zweihander = 2
    hands_to_wield_gladius = 1
    if hands_to_wield_gladius < hands_to_wield_zweihander:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())