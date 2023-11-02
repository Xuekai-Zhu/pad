def solution():
    num_tomato_kinds = 3
    num_tomatoes_per_kind = 5

    num_cucumber_kinds = 5
    num_cucumbers_per_kind = 4

    num_potatoes = 30

    num_rows = 10
    num_spaces_per_row = 15

    # Calculate the total number of spaces for vegetables in the garden
    total_spaces = num_rows * num_spaces_per_row

    # Calculate the total number of spaces already used in the garden
    used_spaces = (num_tomato_kinds * num_tomatoes_per_kind) + \
                  (num_cucumber_kinds * num_cucumbers_per_kind) + \
                  num_potatoes

    # Calculate the number of remaining spaces for vegetables
    remaining_spaces = total_spaces - used_spaces
    result = remaining_spaces
    return result

print(solution())