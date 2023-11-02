def solution():
    """Hayden has a tank with a small hole in the bottom. The tank starts with 40 gallons of water. It loses 2 gallons of water per hour. Hayden does not add any water for the first two hours. He adds 1 gallon of water to the tank in hour three. He adds three gallons of water to the tank in the fourth hour. How much water is left in the tank at the end of the fourth hour?"""
    starting_water = 40
    water_loss_per_hour = 2
    water_added_hour_3 = 1
    water_added_hour_4 = 3
    total_water_loss = water_loss_per_hour * 4
    total_water_added = water_added_hour_3 + water_added_hour_4
    final_water_amount = starting_water - total_water_loss + total_water_added
    result = final_water_amount
    return result

print(solution())