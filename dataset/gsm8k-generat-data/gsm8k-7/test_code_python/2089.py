def solution():
    fraction_left = 1 - 1/6
    weight_left = 1200
    weight_total = weight_left / fraction_left
    weight_eaten = weight_total - weight_left
    result = weight_eaten
    return result

print(solution())