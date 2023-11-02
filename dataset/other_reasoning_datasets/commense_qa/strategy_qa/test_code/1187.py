def solution():
    # Define the dimensions of Alcatraz Island and a football field
    alcatraz_length = 511
    alcatraz_width = 180
    football_field_length = 91
    football_field_width = 48
    # Check if the football field can fit in Alcatraz Island
    if football_field_length <= alcatraz_length and football_field_width <= alcatraz_width:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())