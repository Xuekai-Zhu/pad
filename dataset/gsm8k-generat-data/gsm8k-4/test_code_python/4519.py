def solution():
    """Mari made 4 more than five times as many decorated buttons as Kendra. Sue made half as many as Kendra. Sue made 6 buttons. How many did Mari make?"""
    # Determine the number of buttons made by Sue
    sue_buttons = 6

    # Determine the number of buttons made by Kendra
    kendra_buttons = sue_buttons * 2

    # Determine the number of buttons made by Mari
    mari_buttons = 5 * kendra_buttons + 4

    result = mari_buttons
    return result

print(solution())