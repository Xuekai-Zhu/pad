def solution():
    jack_weight = 60
    anna_weight = 40
    desired_weight = (jack_weight + anna_weight) / 2
    weight_of_rock = 4
    number_of_rocks = (desired_weight - jack_weight) / weight_of_rock
    result = number_of_rocks
    return result

print(solution())