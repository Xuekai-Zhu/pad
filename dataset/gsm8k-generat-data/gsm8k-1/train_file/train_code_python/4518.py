def solution():
    """Mari made 4 more than five times as many decorated buttons as Kendra. Sue made half as many as Kendra. 
    Sue made 6 buttons. How many did Mari make?"""
    sue_buttons = 6
    kendra_buttons = sue_buttons * 2
    mari_buttons = (5 * kendra_buttons) + 4
    result = mari_buttons
    return result

print(solution())