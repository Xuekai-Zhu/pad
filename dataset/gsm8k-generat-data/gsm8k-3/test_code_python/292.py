def solution():
    """A family has three adults and children, both girls and boys. They went out for a family trip and prepared 3 dozen boiled eggs for the trip. Every adult got 3 eggs, and the boys each received 1 more egg than each girl since the girls had some snacks. How many boys went on the trip if the number of girls was 7 and each girl received an egg?"""
    # Define the number of adults and dozens of eggs prepared
    num_adults = 3
    num_eggs = 3 * 12

    # Calculate the number of eggs given to each adult
    eggs_per_adult = 3
    total_eggs_for_adults = num_adults * eggs_per_adult

    # Calculate the number of eggs left for the children
    eggs_for_children = num_eggs - total_eggs_for_adults

    # Calculate the number of girls on the trip
    num_girls = 7
    eggs_per_girl = 1
    total_eggs_for_girls = num_girls * eggs_per_girl

    # Calculate the total number of eggs given to the boys
    eggs_for_boys = eggs_for_children - total_eggs_for_girls

    # Calculate the number of boys on the trip
    boys_per_girl = 1
    num_boys = eggs_for_boys // boys_per_girl

    # Display the number of boys on the trip
    result = num_boys
    return result

print(solution())