def solution():
    """Kimberly went hiking and took a 4-liter bottle full of water with her. The first time she drank from it, she consumed a quarter of the water in the bottle. Later on, she drank 2/3rd of the remaining water. How much water is left in the bottle (in liters)?"""
    
    # Define the initial amount of water in the bottle
    initial_water = 4

    # Calculate the amount of water drank in the first round
    first_round = initial_water * 0.25

    # Calculate the amount of water remaining after the first round
    remaining_water = initial_water - first_round

    # Calculate the amount of water drank in the second round
    second_round = remaining_water * (2/3)

    # Calculate the amount of water remaining after the second round
    final_water = remaining_water - second_round

    # Display the amount of water left in the bottle
    result = final_water
    return result

print(solution())