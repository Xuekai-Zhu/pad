def solution():
    """Every year, Tabitha adds a new color to her hair. She started this tradition when she was 15 years old, which was the year she added her second hair color. In three years, Tabitha will have 8 different colors in the hair. Currently, how old is Tabitha?"""
    starting_year = 15
    starting_colors = 2
    total_colors_in_three_years = 8
    current_age = starting_year + (total_colors_in_three_years - starting_colors)
    result = current_age
    return result

print(solution())