def solution():
    """Chip takes 2 pages of notes every day, 5 days a week, for each of his 5 classes. His notebook paper comes in packs of 100 sheets of paper per pack. After 6 weeks, how many packs of notebook paper will Chip use?"""
    pages_per_day = 2 * 5  # 10 pages per day
    classes_per_day = 5
    sheets_per_pack = 100
    weeks = 6
    total_pages = pages_per_day * classes_per_day * weeks
    total_packs = total_pages / sheets_per_pack
    result = total_packs
    return result

print(solution())