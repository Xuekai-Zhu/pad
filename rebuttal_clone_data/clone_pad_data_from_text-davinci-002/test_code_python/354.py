def solution():
    boxes_left = 4
    boxes_given_away = boxes_left / 2
    boxes_bought = boxes_left + boxes_given_away
    result = boxes_bought
    return result

print(solution())