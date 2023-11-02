def solution():
    """Hannah fills her kids' stockings with 4 candy canes, 2 beanie babies and 1 book. If she has 3 kids, how many stocking stuffers does she buy total?"""
    candy_canes_per_stocking = 4
    beanie_babies_per_stocking = 2
    books_per_stocking = 1
    items_per_stocking = candy_canes_per_stocking + beanie_babies_per_stocking + books_per_stocking
    num_of_kids = 3
    total_items = items_per_stocking * num_of_kids
    result = total_items
    return result

print(solution())