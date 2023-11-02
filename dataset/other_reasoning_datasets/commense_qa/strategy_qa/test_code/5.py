def solution():
    war_duration = 6 # months
    llama_gestation = 11 # months
    llama_births = war_duration // llama_gestation
    if llama_births >= 2:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())