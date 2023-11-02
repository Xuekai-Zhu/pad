def solution():
    fireworks_per_box = 8
    fireworks_per_num = 6
    fireworks_per_letter = 5
    num_boxes = 50 + 1
    num_nums = 4
    num_letters = 7
    total_fireworks = (num_boxes * fireworks_per_box) + (num_nums * fireworks_per_num) + (num_letters * fireworks_per_letter)
    result = total_fireworks
    return result

print(solution())