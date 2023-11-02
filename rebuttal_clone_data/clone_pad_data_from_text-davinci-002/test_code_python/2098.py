def solution():
    hens = 270
    roosters = 3
    eggs_per_hen = 1
    eggs_collected = hens * eggs_per_hen
    eggs_per_box = 6
    boxes_filled = eggs_collected / eggs_per_box
    result = boxes_filled
    return result

print(solution())