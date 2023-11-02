def solution():
    # Calculate the number of cherry lollipops
    cherry_lollipops = 42 / 2

    # Calculate the number of non-cherry lollipops
    non_cherry_lollipops = 42 - cherry_lollipops

    # Calculate the number of non-cherry lollipops that are grape
    grape_lollipops = non_cherry_lollipops / 3

    result = grape_lollipops
    return result

print(solution())