def solution():
    # Set up the variables
    total_children = 180
    boy_ratio = 5
    girl_ratio = 7
    total_ratio = boy_ratio + girl_ratio
    total_boys = (boy_ratio / total_ratio) * total_children
    boy_share = 3900

    # Calculate how much each boy will receive
    each_boy_share = boy_share / total_boys
    result = each_boy_share
    return result

print(solution())