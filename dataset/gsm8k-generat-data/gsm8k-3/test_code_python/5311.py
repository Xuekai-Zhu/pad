def solution():
    """Tim takes his 3 children trick or treating.  They are out for 4 hours. Each hour they visited 5 houses. Each house gives 3 treats per kid.  How many treats do his children get in total?"""
    # Define the number of children, hours, and houses visited per hour
    num_children = 3
    num_hours = 4
    houses_per_hour = 5

    # Define the number of treats each house gives per child
    treats_per_house = 3

    # Calculate the total number of houses visited
    total_houses_visited = num_hours * houses_per_hour

    # Calculate the total number of treats given to each child
    treats_per_child = total_houses_visited * treats_per_house

    # Calculate the total number of treats given to all the children
    total_treats = treats_per_child * num_children

    # Display the total number of treats
    result = total_treats
    return result

print(solution())