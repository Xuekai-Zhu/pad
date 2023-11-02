def solution():
    """There are 26 chickens, 40 piglets, and 34 goats at Stacy’s farm. A really bad storm hits and half of all the animals get sick. How many animals in total get sick?"""
    # Define the number of animals before the storm
    chickens = 26
    piglets = 40
    goats = 34

    # Calculate the number of animals sick after the storm
    sick_chickens = chickens // 2
    sick_piglets = piglets // 2
    sick_goats = goats // 2

    # Calculate the total number of sick animals
    total_sick_animals = sick_chickens + sick_piglets + sick_goats

    # Display the total number of sick animals
    result = total_sick_animals
    return result

print(solution())