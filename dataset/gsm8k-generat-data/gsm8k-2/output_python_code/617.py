def solution():
    """40% of the mosquitos in Jack's area are infected with malaria. 20% of the mosquitos are infected with Zika virus. Without a vaccine, the chances of getting infected with either virus after getting bitten by an infected mosquito are 50%. Jack is taking an experimental malaria vaccine that reduces the chances of getting infected after getting bitten by 50%. If Jack gets bitten by a random mosquito, what is the percentage chance he catches either Zika virus or malaria?"""
    malaria_infected = 0.4
    zika_infected = 0.2
    chance_of_infection = 0.5
    chance_of_malaria = malaria_infected * (1 - 0.5 * chance_of_infection)
    chance_of_zika = zika_infected * (1 - 0.5 * chance_of_infection)
    result = (chance_of_malaria + chance_of_zika) * 100
    return result

print(solution())