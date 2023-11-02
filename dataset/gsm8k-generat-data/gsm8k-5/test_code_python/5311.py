def solution():
    num_children = 3  # Tim has 3 children
    total_time = 4  # They are out for 4 hours
    houses_per_hour = 5  # They visited 5 houses per hour
    treats_per_house = 3 * num_children  # Each house gives 3 treats per kid

    # Calculate the total number of houses visited
    total_houses = houses_per_hour * total_time

    # Calculate the total number of treats the children receive
    total_treats = total_houses * treats_per_house
    result = total_treats
    return result

print(solution())