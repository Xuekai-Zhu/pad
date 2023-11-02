def solution():
    parker_stamps = 18  # Parker originally had 18 stamps
    addie_stamps = 72  # Addie has 72 stamps in total
    addie_gives = addie_stamps / 4  # Addie gives 1/4 of her stamps to Parker
    parker_stamps += addie_gives  # Parker now has the stamps Addie gave him
    result = parker_stamps
    return result

print(solution())