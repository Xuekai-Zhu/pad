def solution():
    """A parking garage of a mall is four stories tall. On the first level, there are 90 parking spaces. The second level has 8 more parking spaces than on the first level, and there are 12 more available parking spaces on the third level than on the second level. The fourth level has 9 fewer parking spaces than the third level. If 100 cars are already parked, how many cars can be accommodated by the parking garage?"""
    first_level_spaces = 90
    second_level_spaces = first_level_spaces + 8
    third_level_spaces = second_level_spaces + 12
    fourth_level_spaces = third_level_spaces - 9
    total_spaces = first_level_spaces + second_level_spaces + third_level_spaces + fourth_level_spaces
    remaining_spaces = total_spaces - 100
    result = remaining_spaces
    return result

print(solution())