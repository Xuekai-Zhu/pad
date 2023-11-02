def solution():
    ginger = 3.0/1
    cardamom = 1.0/3
    mustard = 1.0/3
    garlic = 2.0/3
    chile_powder = 4.0/3
    total_spice = ginger + cardamom + mustard + garlic + chile_powder
    result = (ginger / total_spice) * 100
    return result

print(solution())