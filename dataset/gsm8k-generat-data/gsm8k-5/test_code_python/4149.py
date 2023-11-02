def solution():
    first_level = 90  # First level has 90 parking spaces
    second_level = first_level + 8  # Second level has 8 more parking spaces than the first level
    third_level = second_level + 12  # Third level has 12 more parking spaces than the second level
    fourth_level = third_level - 9  # Fourth level has 9 fewer parking spaces than the third level

    total_spaces = first_level + second_level + third_level + fourth_level  # Total number of parking spaces in the garage
    available_spaces = total_spaces - 100  # Subtract the number of cars already parked to get available spaces

    result = available_spaces
    return result

print(solution())