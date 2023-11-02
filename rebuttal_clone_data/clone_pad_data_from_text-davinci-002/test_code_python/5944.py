def solution():
    normal_corn_per_row = 9
    normal_potatoes_per_row = 30
    destroyed_crops_percentage = 50
    number_of_corn_rows = 10
    number_of_potato_rows = 5
    crops_destroyed_corn = number_of_corn_rows * normal_corn_per_row * (destroyed_crops_percentage / 100)
    crops_destroyed_potatoes = number_of_potato_rows * normal_potatoes_per_row * (destroyed_crops_percentage / 100)
    total_crops_destroyed = crops_destroyed_corn + crops_destroyed_potatoes
    crops_remaining_corn = number_of_corn_rows * normal_corn_per_row - crops_destroyed_corn
    crops_remaining_potatoes = number_of_potato_rows * normal_potatoes_per_row - crops_destroyed_potatoes
    total_crops_remaining = crops_remaining_corn + crops_remaining_potatoes
    result =

print(solution())