def solution():
    """Veronica's flashlight was bright enough to be seen at night from a distance of 1000 feet.  Freddie's flashlight could be seen at night for a distance three times farther than Veronica's flashlight, and Velma's flashlight could be seen at night from a distance 2000 feet less than 5 times farther than Freddie's flashlight.  If Veronica's and Velma's flashlight were placed next to one another and turned on at night, how much farther, in feet, could Velma's flashlight be seen compared to Veronica's?"""
    # Define the distance Veronica's flashlight can be seen
    veronica_distance = 1000

    # Define the distance Freddie's flashlight can be seen
    freddie_distance = veronica_distance * 3

    # Define the distance Velma's flashlight can be seen
    velma_distance = (freddie_distance * 5) - 2000

    # Calculate the difference in distance between Velma's and Veronica's flashlights
    distance_difference = velma_distance - veronica_distance

    # Display the difference in distance
    result = distance_difference
    return result

print(solution())