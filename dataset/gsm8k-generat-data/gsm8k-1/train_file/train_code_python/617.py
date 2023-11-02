def solution():
    """40% of the mosquitos in Jack's area are infected with malaria. 20% of the mosquitos are infected with Zika virus. Without a vaccine, the chances of getting infected with either virus after getting bitten by an infected mosquito are 50%. Jack is taking an experimental malaria vaccine that reduces the chances of getting infected after getting bitten by 50%. If Jack gets bitten by a random mosquito, what is the percentage chance he catches either Zika virus or malaria?"""
    malaria_percent = 0.4
    zika_percent = 0.2
    unvaccinated_chance = 0.5
    vaccinated_chance = 0.25
    chance_of_malaria = (malaria_percent * unvaccinated_chance) + (malaria_percent * vaccinated_chance)
    chance_of_zika = (zika_percent * unvaccinated_chance) + (zika_percent * vaccinated_chance)
    total_chance = chance_of_malaria + chance_of_zika
    result = total_chance * 100
    return result

print(solution())