def solution():
    """Hugo's mountain has an elevation of 10,000 feet above sea level. Boris' mountain has an elevation that is 2,500 feet shorter than Hugo's mountain. If Hugo climbed his mountain 3 times, how many times would Boris need to climb his mountain to have climbed the same number of feet as Hugo?"""
    # Define the elevation of Hugo's mountain
    hugo_elevation = 10000

    # Define the elevation of Boris' mountain
    boris_elevation = hugo_elevation - 2500

    # Calculate the total elevation climbed by Hugo
    total_hugo_elevation = hugo_elevation * 3

    # Calculate the number of times Boris needs to climb his mountain to match Hugo's total elevation
    boris_climbs = total_hugo_elevation / boris_elevation

    # Round up to the nearest whole number of climbs
    boris_climbs = math.ceil(boris_climbs)

    result = boris_climbs
    return result

print(solution())