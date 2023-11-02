def solution():
    """A parking garage of a mall is four stories tall. On the first level, there are 90 parking spaces. The second level has 8 more parking spaces than on the first level, and there are 12 more available parking spaces on the third level than on the second level. The fourth level has 9 fewer parking spaces than the third level. If 100 cars are already parked, how many cars can be accommodated by the parking garage?"""
    level_one = 90
    level_two = level_one + 8
    level_three = level_two + 12
    level_four = level_three - 9
    total_spaces = level_one + level_two + level_three + level_four
    spaces_available = total_spaces - 100
    result = spaces_available
    return result

print(solution())