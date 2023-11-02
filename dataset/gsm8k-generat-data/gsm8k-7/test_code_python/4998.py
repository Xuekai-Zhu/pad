def solution():
    num_years = 3
    num_colors_now = 2
    num_colors_in_three_years = 8

    # Calculate Tabitha's age when she had her first hair color
    first_color_age = 15 - 1  # subtracting 1 since she added her second hair color at age 15

    # Calculate the number of years Tabitha has been adding a new hair color
    num_years_adding_colors = num_colors_in_three_years - num_colors_now

    # Calculate Tabitha's current age
    current_age = first_color_age + num_years_adding_colors
    result = current_age
    return result

print(solution())