def solution():
    is_pope_requirement_met = True
    is_belief_in_one_god_met = True
    is_agnosticism_compatible = False
    if is_pope_requirement_met and is_belief_in_one_god_met and not is_agnosticism_compatible:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())