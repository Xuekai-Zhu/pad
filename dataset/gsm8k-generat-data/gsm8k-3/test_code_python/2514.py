def solution():
    """Hugo's mountain has an elevation of 10,000 feet above sea level.  Boris' mountain has an elevation that is 2,500 feet shorter than  Hugo's mountain.  If Hugo climbed his mountain 3 times, how many times would Boris need to climb his mountain to have climbed the same number of feet as Hugo?"""
    # Define Hugo's mountain elevation in feet
    HUGO_ELEVATION = 10000

    # Define Boris' mountain elevation in terms of Hugo's
    BORIS_ELEVATION = HUGO_ELEVATION - 2500

    # Calculate the total number of feet Hugo climbed
    hugo_climbed = HUGO_ELEVATION * 3

    # Calculate the number of times Boris needs to climb to match Hugo's elevation
    boris_climbs = hugo_climbed / BORIS_ELEVATION

    # Display the number of times Boris needs to climb
    result = boris_climbs
    return result

print(solution())