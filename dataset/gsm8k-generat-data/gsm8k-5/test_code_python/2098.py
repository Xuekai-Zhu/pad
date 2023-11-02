def solution():
    # Calculate the total number of eggs collected per day
    eggs_per_day = 270  # There are 270 hens
    eggs_per_day += 3  # There are also 3 roosters, but they don't lay eggs
    eggs_per_week = eggs_per_day * 7  # Ms. Mosel collects eggs every day of the week

    # Calculate the number of boxes filled each week
    eggs_per_box = 6  # Ms. Mosel puts 6 eggs in each box
    boxes_per_week = eggs_per_week // eggs_per_box  # Round down to the nearest whole number

    result = boxes_per_week
    return result

print(solution())