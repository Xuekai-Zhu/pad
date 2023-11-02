def solution():
    """Dexter and Jay are using a gallon of white paint to paint the walls. Dexter used 3/8 of the gallon of paint while Jay used 5/8 of a gallon of paint. If a gallon is equal to 4 liters, how many liters of paint were left from Dexter and Jay combined?"""
    total_gallons = 1
    dexter_used = 3/8
    jay_used = 5/8
    total_used = dexter_used + jay_used
    total_left = total_gallons - total_used
    liters_per_gallon = 4
    total_liters_left = total_left * liters_per_gallon
    result = total_liters_left
    return result

print(solution())