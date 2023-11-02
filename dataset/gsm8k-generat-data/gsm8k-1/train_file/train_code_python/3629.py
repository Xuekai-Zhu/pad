def solution():
    """A construction company is building 2 apartment buildings with 12 floors each. The apartments are almost ready to sell but all of them need doors to be completed. Each floor has 6 apartments, and each apartment needs 7 doors in total. How many doors does the company need to buy?"""
    num_buildings = 2
    num_floors = 12
    apartments_per_floor = 6
    doors_per_apartment = 7
    num_apartments = num_floors * apartments_per_floor * num_buildings
    num_doors = num_apartments * doors_per_apartment
    result = num_doors
    return result

print(solution())