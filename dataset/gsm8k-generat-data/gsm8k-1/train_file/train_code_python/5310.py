def solution():
    """Tim takes his 3 children trick or treating. They are out for 4 hours. Each hour they visited 5 houses. Each house gives 3 treats per kid. How many treats do his children get in total?"""
    num_children = 3
    num_hours = 4
    houses_per_hour = 5
    treats_per_house = 3
    total_treats = num_children * num_hours * houses_per_hour * treats_per_house
    result = total_treats
    return result

print(solution())