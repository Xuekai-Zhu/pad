def solution():
    """Hugo's mountain has an elevation of 10,000 feet above sea level. Boris' mountain has an elevation that is 2,500 feet shorter than Hugo's mountain. If Hugo climbed his mountain 3 times, how many times would Boris need to climb his mountain to have climbed the same number of feet as Hugo?"""
    hugo_elevation = 10000
    boris_elevation = hugo_elevation - 2500
    hugo_climbs = 3
    boris_climbs = (hugo_climbs * hugo_elevation) / boris_elevation
    result = boris_climbs
    return result

print(solution())