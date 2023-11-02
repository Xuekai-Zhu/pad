def solution():
    """40% of the mosquitos in Jack's area are infected with malaria. 20% of the mosquitos are infected with Zika virus. Without a vaccine, the chances of getting infected with either virus after getting bitten by an infected mosquito are 50%. Jack is taking an experimental malaria vaccine that reduces the chances of getting infected after getting bitten by 50%. If Jack gets bitten by a random mosquito, what is the percentage chance he catches either Zika virus or malaria?"""
    # Define the percentage of mosquitos infected with malaria and Zika
    MALARIA_PERCENTAGE = 0.4
    ZIKA_PERCENTAGE = 0.2

    # Define the probability of getting infected with either virus after getting bitten by an infected mosquito
    UNVACCINATED_PROBABILITY = 0.5

    # Define the probability of getting infected with either virus after getting bitten by an infected mosquito with the vaccine
    VACCINATED_PROBABILITY = UNVACCINATED_PROBABILITY * 0.5

    # Calculate the probability of getting bitten by an infected mosquito
    infected_mosquito_probability = MALARIA_PERCENTAGE + ZIKA_PERCENTAGE

    # Calculate the probability of getting infected with either virus after getting bitten by an infected mosquito without the vaccine
    unvaccinated_probability = infected_mosquito_probability * UNVACCINATED_PROBABILITY

    # Calculate the probability of getting infected with either virus after getting bitten by an infected mosquito with the vaccine
    vaccinated_probability = infected_mosquito_probability * VACCINATED_PROBABILITY

    # Calculate the total probability of getting infected with either virus
    total_probability = unvaccinated_probability + vaccinated_probability

    # Convert the total probability to a percentage
    percentage_probability = total_probability * 100

    # Display the percentage chance of catching either Zika virus or malaria
    result = percentage_probability
    return result

print(solution())