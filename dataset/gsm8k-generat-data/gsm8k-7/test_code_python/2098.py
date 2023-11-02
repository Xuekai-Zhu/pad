def solution():
    num_hens = 270
    num_roosters = 3
    total_birds = num_hens + num_roosters
    eggs_per_bird = 1
    eggs_per_box = 6
    days_per_week = 7
    hours_per_day = 1 + 40/60  # 1 hour of collection and extra 40 minutes
    boxes_per_week = (total_birds * eggs_per_bird * hours_per_day * days_per_week) / eggs_per_box
    result = boxes_per_week
    return result

print(solution())