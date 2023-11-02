def solution():
    candy_canes_per_stocking = 4  # Hannah fills each stocking with 4 candy canes
    beanie_babies_per_stocking = 2  # Hannah fills each stocking with 2 beanie babies
    books_per_stocking = 1  # Hannah fills each stocking with 1 book
    kids = 3  # Hannah has 3 kids

    # Calculate the total number of stocking stuffers Hannah buys for all her kids
    total_stocking_stuffers = (candy_canes_per_stocking + beanie_babies_per_stocking + books_per_stocking) * kids
    result = total_stocking_stuffers
    return result

print(solution())