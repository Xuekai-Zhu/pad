def solution():
    """Lydia is planning a road trip with her family and is trying to plan a route. She has 60 liters of fuel and she will use all of this during her trip. She isn't sure how much fuel she is going to use in the first third of the trip but she knows she will need a third of all of her fuel for the second third of the trip, and half this amount for the final third of the trip. How much fuel, in liters, can Lydia use in the first third of the trip?"""
    # Define the total amount of fuel
    total_fuel = 60
    
    # Calculate the amount of fuel needed for the second third of the trip
    second_third = total_fuel / 3
    
    # Calculate the amount of fuel needed for the final third of the trip
    final_third = second_third / 2
    
    # Calculate the amount of fuel needed for the first third of the trip
    first_third = total_fuel - second_third - final_third
    
    # return the result
    result = first_third
    return result

print(solution())