def solution():
    starting_length = 24  # Marcia's hair is 24" long at the beginning of the school year
    first_cut = starting_length / 2  # Marcia cuts half of her hair off
    first_growth = 4  # Marcia's hair grows 4" longer
    second_cut = 2  # Marcia cuts off 2" of hair at the end

    # Calculate the final length of Marcia's hair
    final_length = starting_length - first_cut + first_growth - second_cut
    result = final_length
    return result

print(solution())