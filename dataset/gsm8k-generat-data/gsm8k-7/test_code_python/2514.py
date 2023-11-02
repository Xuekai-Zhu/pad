def solution():
    hugo_elevation = 10000
    boris_elevation = hugo_elevation - 2500
    hugo_climbs = 3

    # Calculate the total elevation climbed by Hugo
    hugo_total_elevation = hugo_elevation * hugo_climbs

    # Calculate the number of climbs Boris needs to do to match Hugo's elevation
    boris_climbs = hugo_total_elevation / boris_elevation

    result = boris_climbs
    return result

print(solution())