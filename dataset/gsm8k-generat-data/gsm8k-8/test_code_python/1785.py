def solution():
    total_candies = 90
    lollipops = total_candies / 3
    candy_canes = total_candies - lollipops
    num_boys = lollipops / 3
    num_girls = candy_canes / 2
    total_people = num_boys + num_girls
    result = total_people
    return result

print(solution())