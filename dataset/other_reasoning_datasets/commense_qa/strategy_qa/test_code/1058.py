def solution():
    ice_trading = True
    ice_selling = True
    ice_made_people_rich = False
    if ice_trading and ice_selling:
        ice_made_people_rich = True
    if ice_made_people_rich:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())