def solution():
    # Define the percentage of mosquitos infected with malaria and Zika
    malaria_percentage = 40
    zika_percentage = 20

    # Calculate the percentage of mosquitos not infected with either virus
    neither_percentage = 100 - malaria_percentage - zika_percentage

    # Calculate the chance of getting infected with either virus after a bite
    unvaccinated_chance = 50

    # Calculate the chance of getting infected with either virus after a bite with the vaccine
    vaccinated_chance = unvaccinated_chance / 2

    # Calculate the chance of getting infected with either virus after a bite for each type of mosquito
    malaria_chance = malaria_percentage * vaccinated_chance / 100
    zika_chance = zika_percentage * unvaccinated_chance / 100
    neither_chance = neither_percentage * unvaccinated_chance / 100

    # Calculate the total chance of getting infected with either virus
    total_chance = malaria_chance + zika_chance - malaria_chance * zika_chance / 100

    result = total_chance
    return result

print(solution())