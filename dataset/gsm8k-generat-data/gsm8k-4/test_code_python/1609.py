def solution():
    """Kimberly went hiking and took a 4-liter bottle full of water with her. The first time she drank from it, she consumed a quarter of the water in the bottle. Later on, she drank 2/3rd of the remaining water. How much water is left in the bottle (in liters)?"""
    # Define the initial amount of water in the bottle
    initial_water = 4

    # Define the amount of water consumed in the first round
    first_round_consumption = initial_water * 0.25

    # Calculate the remaining water after the first round
    remaining_water = initial_water - first_round_consumption

    # Calculate the amount of water consumed in the second round
    second_round_consumption = remaining_water * (2/3)

    # Calculate the final amount of water remaining in the bottle
    final_water = remaining_water - second_round_consumption
    
    # return the result
    result = final_water
    return result

print(solution())