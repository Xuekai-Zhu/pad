def solution():
    """Tim takes his 3 children trick or treating. They are out for 4 hours. Each hour they visited 5 houses. Each house gives 3 treats per kid. How many treats do his children get in total?"""
    num_children = 3
    num_hours = 4
    num_houses_per_hour = 5
    num_treats_per_house = 3
    num_treats_per_child = num_houses_per_hour * num_treats_per_house
    total_treats = num_treats_per_child * num_children * num_hours
    result = total_treats
    return result

print(solution())