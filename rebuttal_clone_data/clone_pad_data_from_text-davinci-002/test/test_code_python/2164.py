def solution():
    firecrackers_bought = 48
    firecrackers_confiscated = 12
    firecrackers_defective = (firecrackers_bought - firecrackers_confiscated) / 6
    firecrackers_good = firecrackers_bought - firecrackers_confiscated - firecrackers_defective
    firecrackers_set_off = firecrackers_good / 2
    result = firecrackers_set_off
    return result

print(solution())