def solution():
    """Veronica's flashlight was bright enough to be seen at night from a distance of 1000 feet. Freddie's flashlight could be seen at night for a distance three times farther than Veronica's flashlight, and Velma's flashlight could be seen at night from a distance 2000 feet less than 5 times farther than Freddie's flashlight. If Veronica's and Velma's flashlight were placed next to one another and turned on at night, how much farther, in feet, could Velma's flashlight be seen compared to Veronica's?"""
    veronica_distance = 1000
    freddie_distance = 3 * veronica_distance
    velma_distance = 5 * freddie_distance - 2000
    difference = velma_distance - veronica_distance
    result = difference
    return result

print(solution())