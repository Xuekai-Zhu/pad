def solution():
    # Define the year Buzz Aldrin was born, the current year, and the year home computers were first available for sale
    buzz_aldrin_birth_year = 1930
    current_year = 2020
    home_computer_year = 1977
    # Check if Buzz Aldrin could have owned a computer
    if home_computer_year < buzz_aldrin_birth_year:
        result = "no"
    elif home_computer_year > current_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())