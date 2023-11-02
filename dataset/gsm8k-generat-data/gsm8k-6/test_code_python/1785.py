def solution():
    # Calculate the number of lollipops and candy canes
    lollipops = 90 // 3  # one-third of the candies are lollipops
    candy_canes = 90 - lollipops  # the rest of the candies are candy canes

    # Calculate the number of boys and girls
    boys = lollipops // 3  # each boy receives 3 lollipops
    girls = candy_canes // 2  # each girl receives 2 candy canes

    # Calculate the total number of boys and girls
    total = boys + girls
    result = total
    return result

print(solution())