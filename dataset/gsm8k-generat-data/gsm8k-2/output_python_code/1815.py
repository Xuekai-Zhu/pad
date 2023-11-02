def solution():
    """Johnny is out walking his two dogs at night, and his son joins him for the walk. How many legs' worth of organisms are traveling together for this walk?"""
    johnny = 2 # each dog has 4 legs
    son = 2 # assuming the son has 2 legs
    total_legs = johnny * 4 + son * 2
    result = total_legs
    return result

print(solution())