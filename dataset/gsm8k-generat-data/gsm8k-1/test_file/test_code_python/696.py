def solution():
    """Hannah's city is having a big display of fireworks for the 4th of July. They're going to set off 15 boxes of 20 fireworks each. Hannah's house is at the right angle to see 40% of the city's fireworks. Hannah will also set off 3 boxes of 5 fireworks each in her backyard. How many fireworks will Hannah see in total?"""
    total_city_fireworks = 15 * 20
    hannah_sees = int(total_city_fireworks * 0.4)
    hannah_fireworks = 3 * 5
    total_fireworks = hannah_sees + hannah_fireworks
    result = total_fireworks
    return result

print(solution())