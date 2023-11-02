def solution():
    """Lydia is planning a road trip with her family and is trying to plan a route. She has 60 liters of fuel and she will use all of this during her trip. She isn't sure how much fuel she is going to use in the first third of the trip but she knows she will need a third of all of her fuel for the second third of the trip, and half this amount for the final third of the trip. How much fuel, in liters, can Lydia use in the first third of the trip?"""
    total_fuel = 60
    second_third_fuel = total_fuel / 3
    final_third_fuel = second_third_fuel / 2
    first_third_fuel = total_fuel - second_third_fuel - final_third_fuel
    result = first_third_fuel
    return result

print(solution())