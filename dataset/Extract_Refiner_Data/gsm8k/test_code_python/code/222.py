def solution():
    
    # Define the initial number of each type of card
    fire_type = 30
    grass_type = 20
    water_type = 40

    # Define the number of cards that are lost and bought
    lost_water_type = 8
    bought_grass_type = 14

    # Calculate the new total number of cards
    total_cards = fire_type + grass_type + water_type - lost_water_type + bought_grass_type

    # Calculate the percentage chance of picking a randomly picked card that is a water type
    chance_water_type = (water_type / total_cards) * 100

    # Display the percentage chance
    result = chance_water_type
    return result

print(solution())