def solution():
    christianity_co2_emissions = 2
    satanism_co2_emissions = 2
    christianity_deaths = 3000000
    satanism_deaths = 0
    if christianity_co2_emissions < satanism_co2_emissions and christianity_deaths < satanism_deaths:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())