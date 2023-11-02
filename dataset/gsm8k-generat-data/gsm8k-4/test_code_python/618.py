def solution():
    """40% of the mosquitos in Jack's area are infected with malaria. 20% of the mosquitos are infected with Zika virus. Without a vaccine, the chances of getting infected with either virus after getting bitten by an infected mosquito are 50%. Jack is taking an experimental malaria vaccine that reduces the chances of getting infected after getting bitten by 50%. If Jack gets bitten by a random mosquito, what is the percentage chance he catches either Zika virus or malaria?"""
    # Define the percentage of mosquitoes infected with malaria and Zika
    malaria_infected = 0.4
    zika_infected = 0.2

    # Calculate the probability of getting infected with malaria after getting bitten by an infected mosquito
    malaria_probability = 0.5 * (1 - 0.5)

    # Calculate the probability of getting infected with Zika after getting bitten by an infected mosquito
    zika_probability = 0.5 * (1 - 0.5)

    # Calculate the probability of getting infected with either virus after getting bitten by an infected mosquito
    either_virus_probability = malaria_probability * malaria_infected + zika_probability * zika_infected

    # Calculate the probability of getting infected with either virus after getting bitten by a mosquito, given the vaccine
    vaccinated_either_virus_probability = either_virus_probability * 0.5

    # Calculate the total probability of getting infected with either virus after getting bitten by a mosquito, with or without the vaccine
    total_either_virus_probability = either_virus_probability * (1 - 0.5) + vaccinated_either_virus_probability

    # Convert the probability to a percentage
    percentage = total_either_virus_probability * 100

    # Return the result
    result = percentage
    return result

print(solution())