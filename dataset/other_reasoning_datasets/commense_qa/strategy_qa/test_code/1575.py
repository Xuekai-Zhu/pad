def solution():
    jackfruit_weight = 120
    jackfruit_spikes = True
    is_weapon = False
    if jackfruit_weight >= 10 and jackfruit_spikes:
        is_weapon = True
    if is_weapon:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())