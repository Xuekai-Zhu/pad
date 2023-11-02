def solution():
    """Jack leaves his bathtub's faucet dripping at a rate of 40 ml/minute. Water evaporates from the bathtub at a rate of 200 ml/hour. If he leaves the water running for 9 hours, then dumps out 12 liters, how many milliliters of water are left in the bathtub?"""
    faucet_rate = 40 / 1000 # converting ml/min to L/min
    evaporate_rate = 200 / 1000 # converting ml/hour to L/hour
    fill_volume = 0
    for i in range(9 * 60): # calculating the volume of water filled in 9 hours
        fill_volume += faucet_rate
        fill_volume -= evaporate_rate / 60 # converting L/hour to L/min
    dump_volume = 12
    final_volume = fill_volume - (dump_volume * 1000) # converting L to ml
    result = final_volume
    return result

print(solution())