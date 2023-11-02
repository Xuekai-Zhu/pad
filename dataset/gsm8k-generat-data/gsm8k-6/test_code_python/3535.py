def solution():
    # Calculate the length of Marcia's hair after each stage
    first_cut = 24 / 2  # Half of her hair is cut off, so she has 12" left
    growing_out = first_cut + 4  # Her hair grows out 4 more inches, so she has 16" of hair
    second_cut = growing_out - 2  # Another 2" of hair is cut off, so she has 14" of hair left
    result = second_cut
    return result

print(solution())