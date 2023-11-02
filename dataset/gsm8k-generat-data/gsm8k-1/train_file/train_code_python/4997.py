def solution():
    """Every year, Tabitha adds a new color to her hair. She started this tradition when she was 15 years old, which was the year she added her second hair color. In three years, Tabitha will have 8 different colors in the hair. Currently, how old is Tabitha?"""
    starting_age = 15
    total_colors = 8
    years_passed = total_colors - 2
    current_age = starting_age + years_passed
    result = current_age
    return result

print(solution())