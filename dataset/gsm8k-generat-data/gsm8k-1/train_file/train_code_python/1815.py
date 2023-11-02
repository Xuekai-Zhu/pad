def solution():
    """Johnny is out walking his two dogs at night, and his son joins him for the walk. How many legs' worth of organisms are traveling together for this walk?"""
    number_of_dogs = 2
    number_of_sons = 1
    legs_per_dog = 4
    legs_per_son = 2
    total_legs = (number_of_dogs * legs_per_dog) + (number_of_sons * legs_per_son)
    result = total_legs
    return result

print(solution())