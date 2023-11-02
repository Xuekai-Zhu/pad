def solution():
    malaria_infected = 0.4  # 40% of mosquitos are infected with malaria
    zika_infected = 0.2  # 20% of mosquitos are infected with Zika virus
    not_infected = 1 - malaria_infected - zika_infected  # The remaining mosquitos are not infected

    # Probability of getting infected with either virus without vaccine
    prob_no_vaccine = malaria_infected + zika_infected - (malaria_infected * zika_infected)

    # Probability of getting infected with either virus with vaccine
    prob_with_vaccine = (malaria_infected * 0.5) + zika_infected - ((malaria_infected * zika_infected) * 0.5)

    # Probability of getting infected with either virus for Jack
    prob_jack = (prob_with_vaccine * 0.5) + (prob_no_vaccine * not_infected)

    # Convert probability to percentage
    percentage_chance = prob_jack * 100
    result = percentage_chance
    return result

print(solution())