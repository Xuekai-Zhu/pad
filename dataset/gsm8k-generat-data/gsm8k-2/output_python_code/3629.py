def solution():
    """A construction company is building 2 apartment buildings with 12 floors each. The apartments are almost ready to sell but all of them need doors to be completed. Each floor has 6 apartments, and each apartment needs 7 doors in total. How many doors does the company need to buy?"""
    num_buildings = 2
    num_floors = 12
    num_apts_per_floor = 6
    num_doors_per_apt = 7
    total_doors = num_buildings * num_floors * num_apts_per_floor * num_doors_per_apt
    result = total_doors
    return result

print(solution())