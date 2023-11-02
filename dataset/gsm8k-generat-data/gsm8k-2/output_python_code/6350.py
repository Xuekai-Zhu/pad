def solution():
    """Telegraph Road goes through multiple states and is 162 kilometers long. Pardee Road is 12000 meters long. How many kilometers longer is Telegraph Road than Pardee Road?"""
    telegraph_length = 162
    pardee_length = 12000 / 1000  # convert meters to kilometers
    difference = telegraph_length - pardee_length
    result = difference
    return result

print(solution())