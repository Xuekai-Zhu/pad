def solution():
    foster_farms = 45
    american_summit = 2 * foster_farms
    hormel = 3 * foster_farms
    boudin_butchers = foster_farms / 3
    del_monte = american_summit - 30
    total_donated = foster_farms + american_summit + hormel + boudin_butchers + del_monte
    result = total_donated
    return result

print(solution())