def solution():
    """Hannah fills her kids' stockings with 4 candy canes, 2 beanie babies and 1 book. If she has 3 kids, how many stocking stuffers does she buy total?"""
    # Define the number of candy canes, beanie babies, and books in each stocking
    candy_canes_per_stocking = 4
    beanie_babies_per_stocking = 2
    books_per_stocking = 1

    # Define the number of kids
    num_kids = 3

    # Calculate the total number of stocking stuffers
    total_candy_canes = candy_canes_per_stocking * num_kids
    total_beanie_babies = beanie_babies_per_stocking * num_kids
    total_books = books_per_stocking * num_kids

    total_stocking_stuffers = total_candy_canes + total_beanie_babies + total_books

    result = total_stocking_stuffers
    return result

print(solution())