def solution():
    """A family has three adults and children, both girls and boys. They went out for a family trip and prepared 3 dozen boiled eggs for the trip. Every adult got 3 eggs, and the boys each received 1 more egg than each girl since the girls had some snacks. How many boys went on the trip if the number of girls was 7 and each girl received an egg?"""
    num_adults = 3
    num_girls = 7
    num_eggs = 3 * 12
    adult_eggs = num_adults * 3
    girl_eggs = num_girls
    boy_eggs = (num_eggs - adult_eggs - girl_eggs) / 2
    num_boys = boy_eggs - num_girls
    result = num_boys
    return result

print(solution())