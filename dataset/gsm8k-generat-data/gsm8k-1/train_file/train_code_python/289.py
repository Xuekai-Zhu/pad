def solution():
    """A family has three adults and children, both girls and boys. They went out for a family trip and prepared 3 dozen boiled eggs for the trip. Every adult got 3 eggs, and the boys each received 1 more egg than each girl since the girls had some snacks. How many boys went on the trip if the number of girls was 7 and each girl received an egg?"""
    eggs_per_dozen = 12
    adults = 3
    girls = 7
    total_people = adults + girls
    total_eggs = eggs_per_dozen * 3
    adult_eggs = adults * 3
    girl_eggs = girls
    boy_eggs = total_eggs - (adult_eggs + girl_eggs)
    boys = boy_eggs - girls
    result = boys
    return result

print(solution())