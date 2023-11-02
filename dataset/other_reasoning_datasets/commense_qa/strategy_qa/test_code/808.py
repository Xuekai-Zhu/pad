def solution():
    telescope_uses = ["to view things far away"]
    telescope_instrument_type = "optical"
    if "to hear noise" in telescope_uses or "acoustic" in telescope_instrument_type:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())