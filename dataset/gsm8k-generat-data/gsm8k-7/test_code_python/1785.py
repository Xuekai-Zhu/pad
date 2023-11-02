def solution():
    num_candies = 90

    # Calculate the number of lollipops
    num_lollipops = num_candies / 3

    # Calculate the number of candy canes
    num_candy_canes = num_candies - num_lollipops

    # Calculate the number of boys and girls
    num_boys = num_lollipops / 3
    num_girls = num_candy_canes / 2

    # Calculate the total number of boys and girls
    total = num_boys + num_girls
    result = total
    return result

print(solution())