def solution():
    # Calculate the chance of getting infected with malaria after getting bitten by an infected mosquito
    chance_malaria = 0.4 * 0.5 * 0.5 * 100  # 40% of mosquitos are infected with malaria, no vaccine reduces the chances by 50%, and the chance of getting bitten by an infected mosquito is 50%

    # Calculate the chance of getting infected with Zika virus after getting bitten by an infected mosquito
    chance_zika = 0.2 * 0.5 * 100  # 20% of mosquitos are infected with Zika virus and the chance of getting bitten by an infected mosquito is 50%

    # Calculate the total chance of getting infected with either virus after getting bitten by an infected mosquito with the vaccine
    chance_total = (chance_malaria + chance_zika) / 2  # the vaccine reduces the chance by 50%

    result = chance_total
    return result

print(solution())