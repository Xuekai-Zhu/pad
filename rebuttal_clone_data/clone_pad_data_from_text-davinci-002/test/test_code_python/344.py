def solution():
    mosquito_infection_rate = 40
    mosquito_infection_rate_zika = 20
    chance_of_infection = 50
    chance_of_infection_zika = 50
    chance_of_infection_malaria = ((mosquito_infection_rate / 100) * chance_of_infection) + ((mosquito_infection_rate_zika / 100) * chance_of_infection_zika)
    chance_of_infection_malaria_vaccine = chance_of_infection_malaria * 0.5
    result = chance_of_infection_malaria_vaccine
    return result

print(solution())