def solution():
    red_hats = 6
    blue_boots = 9
    both = 3

    # Calculate the total number of gingerbread cookies
    total = red_hats + blue_boots - both

    # Calculate the percentage of cookies with red hats
    percentage = (red_hats / total) * 100

    result = percentage
    return result

print(solution())