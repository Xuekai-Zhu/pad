def solution():
    num_peas = 6
    num_carrots = 9
    num_corn = 5
    total_kids = num_peas + num_carrots + num_corn

    # Calculate the percentage of kids who prefer corn
    percent_corn = (num_corn / total_kids) * 100
    result = percent_corn
    return result

print(solution())