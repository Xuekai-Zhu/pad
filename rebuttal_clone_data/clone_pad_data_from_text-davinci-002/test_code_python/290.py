def solution():
    """A family has three adults and children, both girls and boys. They went out for a family trip and prepared 3 dozen boiled eggs for the trip. Every adult got 3 eggs, and the boys each received 1 more egg than each girl since the girls had some snacks. How many boys went on the trip if the number of girls was 7 and each girl received an egg?"""
    adults = 3
    eggs_per_adult = 3
    girls = 7
    boys = (eggs_per_adult * adults) - (girls + (girls - 1))
    result = boys
    return result

print(solution())