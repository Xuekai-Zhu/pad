def solution():
    """Kendra made 4 more than five times as many decorated buttons as Mari. Sue made half as many as Kendra. Mari made 8 buttons. How many did Sue make?"""
    mari_buttons = 8
    kendra_buttons = 5 * mari_buttons + 4
    sue_buttons = kendra_buttons / 2
    result = sue_buttons
    return result

print(solution())