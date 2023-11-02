def solution():
    """A water tower that serves four neighborhoods around it holds 1200 barrels of water and is filled to the top each week. If one neighborhood uses 150 barrels of water in a week, the second neighborhood uses twice as many barrels of water as the first neighborhood in a week, and the third neighborhood uses one hundred more barrels of water than the second neighborhood in a week, how many barrels are left for the fourth neighborhood?"""
    
    # Define the initial amount of water in the tower
    water_in_tower = 1200
    
    # Subtract the amount of water used by the first neighborhood
    water_in_tower -= 150
    
    # Calculate the amount of water used by the second neighborhood
    neighborhood_two_water = 2 * 150
    
    # Subtract the amount of water used by the second neighborhood
    water_in_tower -= neighborhood_two_water
    
    # Calculate the amount of water used by the third neighborhood
    neighborhood_three_water = neighborhood_two_water + 100
    
    # Subtract the amount of water used by the third neighborhood
    water_in_tower -= neighborhood_three_water
    
    # The amount of water left for the fourth neighborhood is the water that remains in the tower
    water_for_fourth_neighborhood = water_in_tower
    
    # return the result
    result = water_for_fourth_neighborhood
    return result

print(solution())