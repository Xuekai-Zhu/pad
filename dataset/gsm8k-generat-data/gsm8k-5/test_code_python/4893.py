def solution():
    num_boys = 40  # Camp Cedar has 40 boys
    num_girls = 3 * num_boys  # Camp Cedar has 3 times as many girls as boys
    total_children = num_boys + num_girls  # The total number of children at Camp Cedar
    counselors_needed = total_children / 8  # There is 1 counselor needed for every 8 children

    result = counselors_needed
    return result

print(solution())