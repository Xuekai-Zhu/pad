def solution():
    # Counting the tiles twice counts as two separate counts
    tile_count = 2

    # Counting the books three times counts as three separate counts
    book_count = 3

    # Total count for Tuesday is the sum of the separate counts for tiles and books
    total_count = tile_count + book_count

    result = total_count
    return result

print(solution())