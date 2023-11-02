def solution():
    """Every year, Tabitha adds a new color to her hair. She started this tradition when she was 15 years old, which was the year she added her second hair color. In three years, Tabitha will have 8 different colors in the hair. Currently, how old is Tabitha?"""
    # Start counting from the year Tabitha added her second hair color
    hair_color_count = 2

    # Keep track of Tabitha's age
    age = 15

    # Keep adding hair colors until there are 8
    while hair_color_count < 8:
        hair_color_count += 1
        age += 1

    result = age
    return result

print(solution())