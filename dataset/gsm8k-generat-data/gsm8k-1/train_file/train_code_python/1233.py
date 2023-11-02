def solution():
    """A bag of pistachios has 80 pistachios in it. 95 percent have shells, and 75 percent of those have shells that are opened. How many pistachios in the bag have shells and have an opened shell?"""
    total_pistachios = 80
    pistachios_with_shells = total_pistachios * 0.95
    pistachios_with_opened_shells = pistachios_with_shells * 0.75
    result = pistachios_with_opened_shells
    return result

print(solution())