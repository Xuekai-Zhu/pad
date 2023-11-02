def solution():
    """Dexter and Jay are using a gallon of white paint to paint the walls. Dexter used 3/8 of the gallon of paint while Jay used 5/8 of a gallon of paint. If a gallon is equal to 4 liters, how many liters of paint were left from Dexter and Jay combined?"""
    gallon_to_liter_ratio = 4
    dexter_used = (3/8) * gallon_to_liter_ratio
    jay_used = (5/8) * gallon_to_liter_ratio
    total_used = dexter_used + jay_used
    total_left = gallon_to_liter_ratio - total_used
    result = total_left
    return result

print(solution())