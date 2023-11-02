def solution():
    """A mountain range has 200 active volcanoes. In a particular year, 20% of the volcanoes exploded in the first two months,
    40% of the remaining exploded by the half of the year, and at the end of the year, another 50% of the volcanoes that hadn't already erupted also exploded. How many mountains are still intact at the end of the year?"""
    
    total_volcanoes = 200
    first_two_months = int(total_volcanoes * 0.2)
    remaining_volcanoes = total_volcanoes - first_two_months
    next_six_months = int(remaining_volcanoes * 0.4)
    remaining_volcanoes = remaining_volcanoes - next_six_months
    last_two_months = int(remaining_volcanoes * 0.5)
    intact_volcanoes = remaining_volcanoes - last_two_months
    result = intact_volcanoes
    return result

print(solution())