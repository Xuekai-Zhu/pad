def solution():
     stickers_per_page = 20
     pages_of_stickers = 12
     stickers_lost = 1
     total_stickers = stickers_per_page * (pages_of_stickers - stickers_lost)
     result = total_stickers
     return result

print(solution())