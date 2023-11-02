def solution():
    ginger_production = 2.8 # in million tons
    baltimore_cargo = 2.8 # in million tons per fiscal quarter
    baltimore_annual_cargo = baltimore_cargo * 4 # assuming four fiscal quarters in a year
    if ginger_production <= baltimore_annual_cargo:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())