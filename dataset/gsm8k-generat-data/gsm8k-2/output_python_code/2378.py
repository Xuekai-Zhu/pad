def solution():
    """Carla needs to bring water to her animals. Each horse needs twice as much water as a pig, and the chickens drink from one tank that needs 30 gallons. How many gallons of water does Carla need to bring if she has 8 pigs and 10 horses and each pig needs 3 gallons of water?"""
    pig_water = 8 * 3
    horse_water = 10 * 6
    total_water = pig_water + horse_water + 30
    result = total_water
    return result

print(solution())