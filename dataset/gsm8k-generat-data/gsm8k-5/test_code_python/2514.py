def solution():
    hugo_elevation = 10000  # Hugo's mountain has an elevation of 10,000 feet
    boris_elevation = hugo_elevation - 2500  # Boris' mountain is 2,500 feet shorter than Hugo's mountain
    hugo_climbs = 3  # Hugo climbs his mountain 3 times

    # Calculate the total elevation climbed by Hugo
    hugo_total_climb = hugo_elevation * hugo_climbs

    # Calculate the number of times Boris needs to climb his mountain to have climbed the same number of feet as Hugo
    boris_climbs = hugo_total_climb / boris_elevation
    result = boris_climbs
    return result

print(solution())