def solution():
    """Lydia is planning a road trip with her family and is trying to plan a route. She has 60 liters of fuel and she will use all of this during her trip. She isn't sure how much fuel she is going to use in the first third of the trip but she knows she will need a third of all of her fuel for the second third of the trip, and half this amount for the final third of the trip. How much fuel, in liters, can Lydia use in the first third of the trip?"""
    # Define the total amount of fuel Lydia has
    total_fuel = 60

    # Calculate the amount of fuel Lydia will use for the second and third thirds of the trip
    second_third_fuel = total_fuel / 3
    final_third_fuel = second_third_fuel / 2

    # Calculate the amount of fuel Lydia has left for the first third of the trip
    first_third_fuel = total_fuel - second_third_fuel - final_third_fuel

    # Display the amount of fuel Lydia can use in the first third of the trip
    result = first_third_fuel
    return result

print(solution())