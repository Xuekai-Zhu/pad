def solution():
    shirts_mon = 4
    shirts_tues = 3
    shirts_wed = 2

    buttons_per_shirt = 5

    total_shirts = shirts_mon + shirts_tues + shirts_wed

    total_buttons = total_shirts * buttons_per_shirt
    result = total_buttons
    return result

print(solution())