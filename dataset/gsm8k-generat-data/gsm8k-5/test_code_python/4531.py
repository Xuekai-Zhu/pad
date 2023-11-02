def solution():
    pages_with_2_photos = 12  # 12 pages hold 2 photos each
    pages_with_3_photos = 9  # 9 pages hold 3 photos each

    total_photos = (pages_with_2_photos * 2) + (pages_with_3_photos * 3)
    result = total_photos
    return result

print(solution())