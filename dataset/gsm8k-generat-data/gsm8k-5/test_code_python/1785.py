def solution():
    total_candies = 90  # Angeli had 90 assorted candies
    lollipops = total_candies // 3  # One-third of the candies were lollipops
    candy_canes = total_candies - lollipops  # The rest were candy canes

    # Calculate how many boys received lollipops
    boys_lollipops = lollipops // 3
    # Calculate how many girls received candy canes
    girls_candy_canes = candy_canes // 2

    # Calculate the total number of boys and girls together
    total_children = boys_lollipops + girls_candy_canes
    result = total_children
    return result

print(solution())