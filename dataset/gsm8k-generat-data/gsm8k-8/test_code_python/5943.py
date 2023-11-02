def solution():
    # Calculate half of the total lollipops and assign to variable
    cherry_lollipops = 42/2

    # Calculate total non-cherry lollipops and divide by 3 to find amount of each flavor
    non_cherry_lollipops = 42 - cherry_lollipops
    grape_lollipops = non_cherry_lollipops / 3

    result = grape_lollipops
    return result

print(solution())