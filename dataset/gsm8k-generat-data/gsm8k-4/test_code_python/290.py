def solution():
    """A family has three adults and children, both girls and boys. They went out for a family trip and prepared 3 dozen boiled eggs for the trip. Every adult got 3 eggs, and the boys each received 1 more egg than each girl since the girls had some snacks. How many boys went on the trip if the number of girls was 7 and each girl received an egg?"""
    # Define the number of adults in the family
    num_adults = 3

    # Define the number of dozens of boiled eggs prepared for the trip
    num_dozen_eggs = 3

    # Calculate the total number of boiled eggs prepared
    num_eggs = num_dozen_eggs * 12

    # Calculate the total number of eggs needed for the adults
    adult_eggs = num_adults * 3

    # Calculate the number of eggs left for the children
    children_eggs = num_eggs - adult_eggs

    # Calculate the number of girls on the trip
    num_girls = 7

    # Calculate the number of eggs each girl received
    girl_eggs = 1

    # Calculate the total number of girl eggs
    total_girl_eggs = num_girls * girl_eggs

    # Calculate the number of eggs left for the boys
    boys_eggs = children_eggs - total_girl_eggs

    # Calculate the number of boys on the trip
    num_boys = boys_eggs // 2

    # return the result
    result = num_boys
    return result

print(solution())