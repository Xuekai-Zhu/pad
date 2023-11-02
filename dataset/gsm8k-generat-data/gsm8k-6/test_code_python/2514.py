def solution():
    # Calculate Boris' mountain elevation and the number of times he needs to climb to match Hugo
    boris_elevation = 10000 - 2500  # Boris' mountain is 2500 feet shorter than Hugo's mountain
    boris_climb_times = 3 * (10000 / boris_elevation)  # calculate the number of times Boris needs to climb his mountain to match Hugo

    result = boris_climb_times
    return result

print(solution())