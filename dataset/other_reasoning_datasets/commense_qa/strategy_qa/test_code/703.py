def solution():
    primate_height = 12 # in inches
    primate_weight = 9 # in pounds
    ruler_length = 12 # in inches
    max_textbook_weight = 6 # in pounds
    # Check if the primate's height and weight are less than the dimensions of a backpack
    if primate_height <= ruler_length and primate_weight <= max_textbook_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())