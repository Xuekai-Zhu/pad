def solution():
    # Define the variables
    num_children = 3
    num_hours = 4
    num_houses_per_hour = 5
    num_treats_per_house = 3

    # Calculate the total number of houses visited
    total_houses = num_hours * num_houses_per_hour

    # Calculate the total number of treats per child
    treats_per_child = total_houses * num_treats_per_house

    # Calculate the total number of treats for all children
    total_treats = treats_per_child * num_children
    result = total_treats
    return result

print(solution())