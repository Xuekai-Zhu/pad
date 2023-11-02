def solution():
    """Barney can perform 45 sit-ups in one minute. Carrie can do twice as many sit-ups per minute as Barney can. And Jerrie can do 5 more sit-ups per minute than Carrie can do. If Barney does sit-ups for 1 minute, and Carrie does sit-ups for two minutes, and Jerrie does sit-ups for three minutes, what would be the combined total number of sit-ups performed?"""
    barney_situps = 45
    carrie_situps = 2 * barney_situps
    jerrie_situps = carrie_situps + 5

    total_situps = (barney_situps * 1) + (carrie_situps * 2) + (jerrie_situps * 3)

    result = total_situps
    return result

print(solution())