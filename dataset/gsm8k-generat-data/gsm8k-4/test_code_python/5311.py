def solution():
    """Tim takes his 3 children trick or treating. They are out for 4 hours. Each hour they visited 5 houses. Each house gives 3 treats per kid. How many treats do his children get in total?"""
    # Define the number of children and hours
    num_children = 3
    num_hours = 4

    # Define the number of houses visited per hour and treats per house
    houses_per_hour = 5
    treats_per_house = 3

    # Calculate the total number of houses visited
    total_houses = num_hours * houses_per_hour

    # Calculate the total number of treats
    total_treats = total_houses * num_children * treats_per_house

    # return the result
    result = total_treats
    return result

print(solution())