def solution():
    koby_boxes = 2
    cherie_boxes = 1
    koby_sparklers = 3
    koby_whistlers = 5
    cherie_sparklers = 8
    cherie_whistlers = 9
    total_sparklers = koby_boxes * koby_sparklers + cherie_boxes * cherie_sparklers
    total_whistlers = koby_boxes * koby_whistlers + cherie_boxes * cherie_whistlers
    total_fireworks = total_sparklers + total_whistlers
    result = total_fireworks
    return result

print(solution())