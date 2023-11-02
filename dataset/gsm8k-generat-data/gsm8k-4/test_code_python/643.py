def solution():
    """Veronica's flashlight was bright enough to be seen at night from a distance of 1000 feet. Freddie's flashlight could be seen at night for a distance three times farther than Veronica's flashlight,
    and Velma's flashlight could be seen at night from a distance 2000 feet less than 5 times farther than Freddie's flashlight.  If Veronica's and Velma's flashlight were placed next to one another 
    and turned on at night, how much farther, in feet, could Velma's flashlight be seen compared to Veronica's?"""
    
    # Veronica's flashlight can be seen from a distance of 1000 feet
    distance_veronica = 1000

    # Freddie's flashlight can be seen three times farther than Veronica's flashlight
    distance_freddie = distance_veronica * 3

    # Velma's flashlight can be seen 2000 feet less than 5 times farther than Freddie's flashlight
    distance_velma = 5 * distance_freddie - 2000

    # Calculate how much farther Velma's flashlight can be seen compared to Veronica's
    distance_difference = distance_velma - distance_veronica

    # return the result
    result = distance_difference
    return result

print(solution())