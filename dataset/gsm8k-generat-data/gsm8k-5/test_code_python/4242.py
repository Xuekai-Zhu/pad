def solution():
    pages_per_comic = 25  # Each comic has 25 pages
    total_pages_found = 150  # Aston found 150 pages on the floor
    comics_repaired = total_pages_found // pages_per_comic  # Number of comics repaired

    # Calculate the total number of comics in the box
    total_comics = comics_repaired + 5  # 5 untorn comics were already in the box

    result = total_comics
    return result

print(solution())