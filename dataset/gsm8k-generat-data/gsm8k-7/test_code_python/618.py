def solution():
    malaria_infected = 0.4
    zika_infected = 0.2
    chance_of_infection_without_vaccine = 0.5
    chance_of_infection_with_vaccine = 0.5 * 0.5  # 50% reduction with vaccine

    # Calculate the chance of getting infected with either virus when bitten by an infected mosquito
    chance_of_malaria = malaria_infected * chance_of_infection_without_vaccine * chance_of_infection_with_vaccine
    chance_of_zika = zika_infected * chance_of_infection_without_vaccine * chance_of_infection_with_vaccine
    chance_of_either = chance_of_malaria + chance_of_zika

    # Convert the chance to a percentage
    percentage_chance = chance_of_either * 100
    result = percentage_chance
    return result

print(solution())