def solution():
    # Calculate the number of buttons made by Kendra
    kendra_buttons = 6 * 2  # Sue made half as many as Kendra, so Kendra made 6 x 2 = 12 buttons
    # Calculate the number of buttons made by Mari
    mari_buttons = 5 * kendra_buttons + 4  # Mari made 4 more than five times as many as Kendra
    result = mari_buttons
    return result

print(solution())