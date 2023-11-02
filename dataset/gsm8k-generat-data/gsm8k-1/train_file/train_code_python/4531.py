def solution():
    """Mr. Reyansh has a dairy farm with 40 cows. Each cow on the farm drinks 80 liters of water daily. 
    He also has a sheep ranch with 10 times the number of cows, with each sheep drinking 1/4 times as much water as a cow does. 
    How many liters of water does Mr. Reyansh use to water all of his animals in a week?"""
    
    cows = 40
    cow_water = 80
    sheep = 10 * cows
    sheep_water = cow_water / 4
    total_water = (cows * cow_water + sheep * sheep_water) * 7
    
    return total_water

print(solution())