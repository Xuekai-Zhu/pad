def solution():
    """Mia can decorate 2 dozen Easter eggs per hour. Her little brother Billy can only decorate 10 eggs per hour. They need to decorate 170 eggs for the Easter egg hunt. If they work together, how long will it take them to decorate all the eggs?"""
    mia_rate = 2 * 12
    billy_rate = 10
    eggs_to_decorate = 170
    combined_rate = mia_rate + billy_rate
    time_to_decorate = eggs_to_decorate / combined_rate
    result = time_to_decorate
    return result

print(solution())