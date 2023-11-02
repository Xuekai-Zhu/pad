def solution():
    """Rebecca makes her own earrings out of buttons, magnets, and gemstones. For every earring, she uses two magnets, half as many buttons as magnets, and three times as many gemstones as buttons. If Rebecca wants to make 4 sets of earrings, how many gemstones will she need?"""
    magnets_per_earring = 2
    buttons_per_earring = magnets_per_earring / 2
    gemstones_per_earring = buttons_per_earring * 3
    total_gemstones = gemstones_per_earring * 2 * 4
    result = total_gemstones
    return result

print(solution())