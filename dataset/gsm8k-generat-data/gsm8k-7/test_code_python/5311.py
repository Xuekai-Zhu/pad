def solution():
    num_children = 3
    num_hours = 4
    houses_visited_per_hour = 5
    treats_per_house_per_child = 3

    # Calculate the total number of houses visited
    total_houses_visited = num_hours * houses_visited_per_hour

    # Calculate the total number of treats received per child
    total_treats_per_child = total_houses_visited * treats_per_house_per_child

    # Calculate the total number of treats received by all children
    total_treats = num_children * total_treats_per_child
    result = total_treats
    return result

print(solution())