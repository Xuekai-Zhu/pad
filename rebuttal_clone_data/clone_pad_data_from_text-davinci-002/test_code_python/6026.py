def solution():
    boxes_bought = 3
    burritos_given = boxes_bought / 3
    burritos_eaten = 3 * 10
    total_burritos = boxes_bought * 20
    burritos_left = total_burritos - burritos_given - burritos_eaten
    result = burritos_left
    return result

print(solution())