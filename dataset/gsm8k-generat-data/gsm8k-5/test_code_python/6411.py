def solution():
    magnets_per_earring = 2  # Rebecca uses 2 magnets per earring
    buttons_per_earring = magnets_per_earring / 2  # Rebecca uses half as many buttons as magnets per earring
    gemstones_per_earring = buttons_per_earring * 3  # Rebecca uses three times as many gemstones as buttons per earring
    earrings_per_set = 2  # Rebecca needs two earrings to make a set
    sets = 4  # Rebecca wants to make 4 sets of earrings

    # Calculate the total number of gemstones needed
    total_gemstones = gemstones_per_earring * earrings_per_set * sets
    result = total_gemstones
    return result

print(solution())