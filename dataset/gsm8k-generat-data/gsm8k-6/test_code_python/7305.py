def solution():
    # Calculate the number of cats in the neighborhood before the twenty new dogs were born
    cats_orig = 20 / 2  # originally, there were twice as many cats as dogs
    dogs_orig = cats_orig / 2  # originally, the number of dogs was half the number of cats

    # Calculate the number of cats in the neighborhood to begin with
    cats_begin = cats_orig - 20  # since twenty new dogs were born

    result = cats_begin
    return result

print(solution())