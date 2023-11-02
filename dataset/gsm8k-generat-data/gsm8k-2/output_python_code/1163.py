def solution():
    """Hayden has a tank with a small hole in the bottom. The tank starts with 40 gallons of water. It loses 2 gallons of water per hour. Hayden does not add any water for the first two hours. He adds 1 gallon of water to the tank in hour three. He adds three gallons of water to the tank in the fourth hour. How much water is left in the tank at the end of the fourth hour?"""
    starting_gallons = 40
    loss_per_hour = 2
    remaining_gallons = starting_gallons - (loss_per_hour * 2)
    remaining_gallons += 1
    remaining_gallons += 3
    result = remaining_gallons
    return result

print(solution())