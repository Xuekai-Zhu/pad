def solution():
    """Elizabeth has 10 reusable water bottles. She loses 2 water bottles at school. Then someone steals 1 of her water bottles at dance practice. To avoid any future theft of her water bottles, Elizabeth places 3 stickers on each of her remaining bottles. How many stickers does Elizabeth use in total on her water bottles?"""
    initial_bottles = 10
    lost_school = 2
    stolen_practice = 1
    remaining_bottles = initial_bottles - lost_school - stolen_practice
    stickers_per_bottle = 3
    total_stickers = remaining_bottles * stickers_per_bottle
    result = total_stickers
    return result

print(solution())